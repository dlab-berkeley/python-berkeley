---
layout: page
title: Past Meetings
comments: true
permalink: /past/
---

## Past Meetings
Here is a list of topics from our previous meetings and associated learning resources.

<div class="all-posts" post-cate="All">
  {% assign curDate = site.time | date: '%s' %}
  {% assign lastYear = curDate | minus: 31536000 | date: "%s" %} <!-- remove post after 1 year --> 
  {% for post in site.posts %}
    {% assign postStartDate = post.date | date: '%s' %}
    {% if postStartDate <= curDate and postStartDate > lastYear %}
      <a class="post-list-item" href="{{ post.url | prepend: site.baseurl }}">
        <h2>
        {{ post.title }}
        </h2>
        <span class="">{{ post.date | date: "%b %-d, %Y" }}</span>
      </a>
    {% endif %}
  {% endfor %}
</div>
