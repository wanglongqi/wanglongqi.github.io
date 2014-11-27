---
layout: page
title: uniUnit
slug: uniUnit
---
[uniUnit](https://github.com/wanglongqi/uniUnit) is a python package providing consistent units for calculation. Here is the support page for the package. The posts related to uniUnit is listed here.

<ul>
1
{% for post in site.categories.site %}
  	{% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
2
{% for post in site.categories.Site %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
3
{% for post in site.categories[site] %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
4
{% for post in site.categories["site"] %}
    {% if post.url %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>
