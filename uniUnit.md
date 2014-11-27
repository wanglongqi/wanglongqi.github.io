---
layout: page
title: Posts related to uniUnit
slug: uniUnit
---
[uniUnit](https://github.com/wanglongqi/uniUnit) is a python package providing consistent units for calculation. Here is the support page for the package. The posts related to uniUnit is listed here.

<ul>
{% for category in site.categories[uniUnit] %}
  <li class="arcat"><a name="{{ category | first }}">{{ category | first }}</a>
    <ul class="arpost">
    {% for posts in category %}
      {% for post in posts %}
      	{% if post.url %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
        {% endif %}
      {% endfor %}
    {% endfor %}
    </ul>
  </li>
{% endfor %}
</ul>
