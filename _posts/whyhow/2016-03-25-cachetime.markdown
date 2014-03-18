---
author: YiZi
comments: true
date: 2016-03-25 10:17:31 +0800
layout: post
slug: cachetime0325
title: Github Page 如何强制刷新内容
categories: [Website]
tags:
-  Jekyll
-  网站相关
-  缓存控制
---
<div class="forward">本文转载自新网站同名文章：<a href="https://whyhow.github.io/2016/03/25/cachetime.html">https://whyhow.github.io/2016/03/25/cachetime.html</a></div>
[Github.io]()是不能设置Cache-Control的，你就算上传了`.htacess`也会被直接忽略。但是一个网站总有些资源是需要实时更新的，这个怎么办呢？下面是一个变通的解决方案：

网站的最新更新是存储在下面的路径下，所以更新右侧的最新文章需要载入`news.json`，但是Github默认的刷新时间是10分钟，所以你将看不到10分钟以内的刷新。虽然也不算特别影响使用，但是还是比较不开心。

{% highlight js %}
$.getJSON('/search/news.json',callback);
{% endhighlight %}

经过一番研究，发现可以通过如下方式获得实时的结果。原理很简单，通过添加一个URL参数，这样浏览器就会认为每次请求的是不同的东西，所以也就没有时间限制了。这里直接使用当前时间作为参数，同样的原理可以将时间设置为缓存时间为1分钟或者2分钟。大于十分钟就没有意义了，因为默认的缓存时间是十分钟。

{% highlight js %}
$.getJSON('/search/news.json?nocache=' + (new Date()).getTime(), callback);
{% endhighlight %}


