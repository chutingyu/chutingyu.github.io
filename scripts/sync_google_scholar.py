#!/usr/bin/env python3
"""Fetch a public Google Scholar profile and write Jekyll-friendly YAML.

The script intentionally keeps its dependencies in Python's standard library so
it can run on a stock GitHub Actions runner.
"""

from __future__ import annotations

import argparse
import html
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen


PROFILE_BASE = "https://scholar.google.com/citations"


@dataclass
class Publication:
    title: str = ""
    authors: str = ""
    venue: str = ""
    year: str = ""
    citations: int = 0
    url: str = ""


class ScholarParser(HTMLParser):
    """Small parser for the stable class names used by Scholar profile rows."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.publications: list[Publication] = []
        self.current: Publication | None = None
        self.row_depth = 0
        self.capture: str | None = None
        self.capture_depth = 0
        self.buffer: list[str] = []
        self.gray_index = 0

    @staticmethod
    def classes(attrs: list[tuple[str, str | None]]) -> set[str]:
        return set(dict(attrs).get("class", "").split())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = self.classes(attrs)
        values = dict(attrs)

        if tag == "tr" and "gsc_a_tr" in classes:
            self.current = Publication()
            self.row_depth = 1
            self.gray_index = 0
            return

        if not self.current:
            return
        self.row_depth += 1

        if tag == "a" and "gsc_a_at" in classes:
            self.capture = "title"
            self.capture_depth = self.row_depth
            self.buffer = []
            self.current.url = urljoin(PROFILE_BASE, values.get("href", ""))
        elif tag == "div" and "gs_gray" in classes:
            self.capture = "authors" if self.gray_index == 0 else "venue"
            self.gray_index += 1
            self.capture_depth = self.row_depth
            self.buffer = []
        elif tag in {"a", "span"} and "gsc_a_ac" in classes:
            self.capture = "citations"
            self.capture_depth = self.row_depth
            self.buffer = []
        elif tag == "span" and "gsc_a_h" in classes:
            self.capture = "year"
            self.capture_depth = self.row_depth
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.current and self.capture:
            self.buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if not self.current:
            return

        if self.capture and self.row_depth == self.capture_depth:
            value = " ".join("".join(self.buffer).split())
            if self.capture == "citations":
                self.current.citations = int(value) if value.isdigit() else 0
            else:
                setattr(self.current, self.capture, value)
            self.capture = None
            self.buffer = []

        if tag == "tr" and self.row_depth == 1:
            if self.current.title:
                self.publications.append(self.current)
            self.current = None
            self.row_depth = 0
            return
        self.row_depth -= 1


def fetch_page(user_id: str, start: int) -> str:
    query = urlencode({
        "user": user_id,
        "hl": "en",
        "cstart": start,
        "pagesize": 100,
    })
    request = Request(
        f"{PROFILE_BASE}?{query}",
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "Chrome/124.0 Safari/537.36"
            ),
            "Accept-Language": "en-AU,en;q=0.9",
        },
    )
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def scrape(user_id: str, fixture: Path | None = None) -> list[Publication]:
    publications: list[Publication] = []
    start = 0
    while True:
        body = fixture.read_text(encoding="utf-8") if fixture else fetch_page(user_id, start)
        if "gsc_a_tr" not in body:
            reason = "Google Scholar returned a verification or rate-limit page"
            raise RuntimeError(reason)

        parser = ScholarParser()
        parser.feed(body)
        if not parser.publications:
            break
        publications.extend(parser.publications)

        if fixture or len(parser.publications) < 100:
            break
        start += 100
        time.sleep(2)

    # Profile pages can occasionally repeat the final row between pages.
    unique: dict[tuple[str, str], Publication] = {}
    for publication in publications:
        unique[(publication.title.casefold(), publication.year)] = publication
    return sorted(
        unique.values(),
        key=lambda item: (int(item.year) if item.year.isdigit() else 0, item.title.casefold()),
        reverse=True,
    )


def yaml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    escaped = escaped.replace("\n", " ").replace("\r", " ")
    return f'"{escaped}"'


def render_yaml(user_id: str, publications: list[Publication]) -> str:
    lines = [
        f'profile_url: "{PROFILE_BASE}?user={user_id}&hl=en"',
        f'updated_at: "{datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}"',
        "publications:",
    ]
    for publication in publications:
        lines.extend([
            f"  - title: {yaml_string(html.unescape(publication.title))}",
            f"    authors: {yaml_string(html.unescape(publication.authors))}",
            f"    venue: {yaml_string(html.unescape(publication.venue))}",
            f"    year: {yaml_string(publication.year)}",
            f"    citations: {publication.citations}",
            f"    url: {yaml_string(publication.url)}",
        ])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", default="yhKNG0kAAAAJ")
    parser.add_argument("--output", type=Path, default=Path("_data/google_scholar_publications.yml"))
    parser.add_argument("--fixture", type=Path, help="Parse a saved Scholar page instead of making a request")
    args = parser.parse_args()

    try:
        publications = scrape(args.user, args.fixture)
    except Exception as error:
        print(f"Scholar sync failed: {error}", file=sys.stderr)
        return 1

    if not publications:
        print("Scholar sync failed: no publications found", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_yaml(args.user, publications), encoding="utf-8")
    print(f"Wrote {len(publications)} publications to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
