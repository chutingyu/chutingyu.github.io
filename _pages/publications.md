---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
{% include base_path %}
## Major Peer-reviewed Conference and Journal Papers

{% for post in site.publications reversed %}
  {% capture pub_type %}{{ post.pub_type }}{% endcapture %}
  {% if pub_type == "major_publication" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Minor Lightly-Reviewed Posters, Extended Abstracts, and Workshop Papers

{% for post in site.publications reversed %}
  {% capture pub_type %}{{ post.pub_type }}{% endcapture %}
  {% if pub_type == "minor_publication" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
