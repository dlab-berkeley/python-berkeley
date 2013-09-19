---
layout: default
title: Py4Science at UC Berkeley
---

---
Next Meeting: **{{ site.py4sci }}**.<br>
Meetings take place at the [D-Lab](http://dlab.berkeley.edu) from 5-7pm.

These meetings are announced on the [py4science mailing
list](https://calmail.berkeley.edu/manage/list/listinfo/py4science@lists.berkeley.edu).
Sign up there to stay tuned. There's also a
[calendar](https://www.google.com/calendar/embed?src=moeh9ilpdjicogfaav9jtplh28%40group.calendar.google.com&ctz=America/Los_Angeles) 

---
{% for post in site.categories.py4science %}

<h2> <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
 
({{ post.date | date_to_long_string}}) </h2>

{{ post.content }}

---
{% endfor %}


