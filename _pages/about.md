---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% include base_path %}

<img src="images/uq-banner.png" alt="uq-banner" width="200"/>

# About Me

Chuting Yu (Veronica) is a PhD student at the <a href="http://ielab.io/" target="_blank">Information Engineering Lab (IELab)</a> in the <a href="https://eecs.uq.edu.au/" target="_blank">School of Electrical Engineering and Computer Science</a> at the <a href="https://www.uq.edu.au/" target="_blank">University of Queensland</a>, Australia, where she works closely with <a href="https://ielab.io/people/teerapong-leelanupab" target="_blank">Dr. Teerapong Leelanupab</a>, <a href="https://jmmackenzie.io" target="_blank">Dr. Joel Mackenzie</a>, and <a href="https://ielab.io/people/guido-zuccon.html" target="_blank">Professor Guido Zuccon</a>.

Prior to commencing her PhD, Chuting received her Bachelor of Science in Information and Computing Science from <a href="https://www.nbt.edu.cn/" target="_blank">NingboTech University</a>, China, in 2020. She subsequently completed her Master's degree in Software Engineering at the University of Queensland in 2021.

Chuting's research focuses on **Information Retrieval (IR)**, particularly the use of **Large Language Models (LLMs)** for assessment and evaluation. Her work investigates the reliability, robustness, and consistency of LLM-based judgments. She is particularly interested in understanding the limitations of LLM-as-a-Judge approaches and developing more reliable and efficient LLM-based evaluation methods.

Chuting publishes her research at leading international conferences in Information Retrieval, including SIGIR and ECIR.


# News
<b>2025-10-01</b> <br> 🏫 I am thrilled to announce that I will be joining <a href="http://ielab.io/" target="_blank">IELab</a> @ <a href="https://www.uq.edu.au/" target="_blank">UQ</a> as an MPhil student!
<details class="page__news">
  <summary>MORE...</summary>
  <ul>
    <li>...</li>
  </ul>
</details>

<br>

# Travel

* <b>2026-07-20 – 2026-07-24</b> <br> ✈️ Melbourne, Australia for SIGIR 2026

* <b>2025-12-07 – 2025-12-10</b> <br> ✈️ Brisbane, Australia for SIGIR-AP 2025 (Brisbane Satellite Venue)

* <b>2022-07-11 – 2022-07-15</b> <br> ✈️ Madrid, Spain for SIGIR 2022 (Attending Online)

<details class="page__travel">
  <summary>MORE...</summary>
  <ul>
    <li>...</li>
  </ul>
</details>

<br>

# Recent Publications

{% assign recent_publications = site.data.google_scholar_publications.publications %}
{% for publication in recent_publications limit:3 %}
<article class="archive__about" itemscope itemtype="http://schema.org/CreativeWork">
  <h2 class="archive__about-title" itemprop="headline">
    <a href="{{ publication.url }}" target="_blank" rel="noopener">{{ publication.title }}</a>
  </h2>
  {{ publication.authors }}<br>
  {{ publication.venue }}<br>
  {% if publication.citations > 0 %}Cited by {{ publication.citations }}{% endif %}
</article>
{% endfor %}

<p><a href="{{ base_path }}/publications/">View all publications →</a></p>
