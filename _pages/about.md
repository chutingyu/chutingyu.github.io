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

Chuting Yu is an MPhil student at <a href="http://ielab.io/" target="_blank">IELab</a> in the <a href="https://eecs.uq.edu.au/" target="_blank">School of Electrical Engineering and Computer Science</a> at the <a href="https://www.uq.edu.au/" target="_blank">University of Queensland</a>, Australia, where she works closely with <a href="https://ielab.io/people/teerapong-leelanupab" target="_blank">Dr. Teerapong Leelanupab</a> and <a href="https://jmmackenzie.io" target="_blank">Dr. Joel Mackenzie</a>. Prior to Ph.D, Chuting received her Bachelor of Science degree in <a href="https://www.nbt.edu.cn/" target="_blank">Information and Computing Science</a> at the Ningbo Institute of Technology (NIT) in China in 2020. After Bachelor's degree, Chuting went to the University of Queensland for a Master's degree in Software Engineering, she completed the study and awarded Master's degree in 2021.

Chuting works at the intersection of **Information Retrieval**, **Natural Language Processing (NLP)**, and **Machine Learning (ML)** applications in the medical domain, where she utilises **different machine learning models** to empower the **search effectiveness**. Her recent work seeks to address the **gap** between **medical record search** and **deep language models**, through different approaches that helps to improve the search system effectiveness with **minimal efficiency cost**.

Chuting publishes at premier academic venues in IR (e.g. SIGIR, ECIR).


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
