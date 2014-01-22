---
layout: page
title: Python Events at Cal
---

{% for post in site.categories.events %}
---
<h2> <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>

({{ post.date | date_to_long_string}}) </h2>

{{ post.content }}

{% endfor %}


