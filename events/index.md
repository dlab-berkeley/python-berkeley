---
layout: page
title: Python Events at Cal
---

{% for post in site.categories.events %}
  {{ DIVIDER }}
  *{{ post.date | date_to_long_string}}*

## [{{ post.title }}]({{ site.url }}{{ post.url }})

  {{ post.content }}

  {% assign DIVIDER = "---" %}
{% endfor %}


