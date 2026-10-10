---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
{% include base_path %}
{% assign scholar = site.data.google_scholar_publications %}

<p class="scholar-intro">
  Publications are automatically synced from
  <a href="{{ scholar.profile_url }}" target="_blank" rel="noopener">Google Scholar</a>.
  <small>Last synced: {{ scholar.updated_at }}</small>
</p>

{% assign publications_by_year = scholar.publications | group_by: "year" %}
{% for year in publications_by_year %}
## {{ year.name }}

  {% for publication in year.items %}
<article class="scholar-publication">
  <h3><a href="{{ publication.url }}" target="_blank" rel="noopener">{{ publication.title }}</a></h3>
  <p class="scholar-authors">{{ publication.authors }}</p>
  <p class="scholar-venue">{{ publication.venue }}</p>
  {% if publication.citations > 0 %}<p class="scholar-citations">Cited by {{ publication.citations }}</p>{% endif %}
</article>
  {% endfor %}
{% endfor %}

<style>
  .scholar-intro small { display: block; margin-top: .25rem; color: #666; }
  .scholar-publication { margin: 0 0 1.5rem; }
  .scholar-publication h3 { margin-bottom: .3rem; font-size: 1.05em; }
  .scholar-publication p { margin: .15rem 0; }
  .scholar-authors { color: #333; }
  .scholar-venue, .scholar-citations { color: #666; font-size: .9em; }
</style>
