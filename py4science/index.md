---
layout: default
title: Py4Science at UC Berkeley
---

---
Next Meeting: **{{ site.py4sci }}**.<br>
Meetings take place at the [D-Lab](http://dlab.berkeley.edu) from 5-7pm.

---
{% for post in site.categories.py4science %}

<h2> <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
 
({{ post.date | date_to_long_string}}) </h2>

{{ post.content }}

---
{% endfor %}


