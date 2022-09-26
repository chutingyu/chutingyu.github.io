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

Chuting Yu is currently a PhD student at <a href="http://ielab.io/" target="_blank">IELab</a> in the <a href="https://itee.uq.edu.au/" target="_blank">School of Information Technology and Electrical Engineering</a> at the <a href="https://www.uq.edu.au/" target="_blank">University of Queensland</a>, Australia, where she works closely with <a href="http://ielab.io/people/guido-zuccon" target="_blank">A/Prof. Guido Zuccon</a> and <a href="http://bevankoopman.github.io/" target="_blank">Dr. Bevan Koopman</a>. Prior to Ph.D, Chuting received her Bachelor of Science degree in <a href="https://www.nbt.edu.cn/" target="_blank">Information and Computing Science</a> at the Ningbo Institute of Technology (NIT) in China in 2020. After Bachelor's degree, Chuting went to the University of Queensland for a Master's degree in Software Engineering, she completed the study and awarded Master's degree in 2021.

Chuting works at the intersection of **Information Retrieval**, **Natural Language Processing (NLP)**, and **Machine Learning (ML)** applications in the medical domain, where she utilises **different machine learning models** to empower the **search effectiveness**. Her recent work seeks to address the **gap** between **medical record search** and **deep language models**, through different approaches that helps to improve the search system effectiveness with **minimal efficiency cost**.

Chuting publishes at premier academic venues in IR (e.g. SIGIR, ECIR).


# News
<b>2022-09-10</b> <br> 🏫 I am thrilled to announce that I will be joining <a href="http://ielab.io/" target="_blank">IELab</a> @ <a href="https://www.uq.edu.au/" target="_blank">UQ</a> as a Ph.D student in Information Retrieval under the supervision of <a href="http://ielab.io/people/guido-zuccon" target="_blank">A/Prof. Guido Zuccon</a> starting next month!
<details class="page__news">
  <summary>MORE...</summary>
  <ul>
    <li>...</li>
  </ul>
</details>

<br>

# Travel

* <b>2022-07-11 -- 2022-07-15</b> <br> ✈️ Madrid, Spain for SIGIR 2022 (Attending Online)

<details class="page__travel">
  <summary>MORE...</summary>
  <ul>
    <li>...</li>
  </ul>
</details>

<br>

# Recent Publications

{% for post in site.publications reversed %}
  {% capture pub_type %}{{ post.pub_type }}{% endcapture %}
  {% if pub_type == "major_publication" %}
    {% include archive-single-about.html %}
  {% endif %}
{% endfor %}
