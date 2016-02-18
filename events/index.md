---
layout: page
---
<!-- title: Python Events at Cal (OLD, SO NOT SHOWING UP IN NAV BAR) 
 -->
{% for post in site.categories.events %}
  {{ DIVIDER }}
  *{{ post.date | date_to_long_string}}*

## [{{ post.title }}]({{ site.url }}/learnpython{{ post.url }})

  {{ post.content }}

  {% assign DIVIDER = "---" %}
{% endfor %}


