---
layout: page
title: 文章目录
slug: Archive
---

## Blog Posts

{% for post in site.posts %}
  * {{ post.date | date_to_string }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}

{% for category in site.categories %}
    <li style="font-size: {{ category | last | size | times: 100 | divided_by: site.categories.size }}%">
        <a href="/{{ category | first | slugize }}/">
            {{ category | first }}
        </a>
    </li>
{% endfor %}