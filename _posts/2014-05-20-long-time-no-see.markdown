---
layout: post
title: "Long Time No See"
date: 2014-05-20T21:01:23+08:00
---

This site is not updated for a long time. What am I doing these days? Fine, I am busy with my examinations and after that I am following several Coursea lectures on Data Analysis. Although I am not a new user in Data Analysis, I can still learn many things by participating the courses. If you are interested, you can check my gibhub repositories. There are many courses related repositories in the list. All the codes are written in R, which is a statisticial domain specific language. It is very handy to use R to process data for statistics. I use it time to time. However, I still think Python is a better language for most of the purpose. 

Two Python scripts are uploaded to [Misc](https://github.com/wanglongqi/Misc) repository. Both of them are used obtain links from specific websites. `edown.py` download ed2k links from [simplecd.me]. `shadowsocks.py` download shadowsocks server information from [shadowsocks.net].

These two scripts are pretty simple. Load the webpage by `urllib2`, then extract information by using XPath.

{% highlight python %}
from lxml import etree
import urllib2
import subprocess

parser = etree.HTMLParser()
doc=urllib2.urlopen(url).read()
tree=etree.fromstring(doc,parser)
tree.xpath('//a')
{% endhighlight %}
