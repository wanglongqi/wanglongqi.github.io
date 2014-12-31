---
author: Longqi
comments: true
date: 2014-12-31 10:13:31
layout: post
slug: RemoveLegendinggplot
title: ggplot移除Legend
categories: [R]
tags:
- ggplot
- R
- Tutorial
---
![TextPlot](/public/images/textplot.png)
ggplot默认提供了适合正常情况的legend，但是有些时候legend有点多余，那么怎么样来删除legend呢？

有三种方法：

1. 使用`guides(fill=FALSE)`，或者`guides(color=FALSE)`。取决于需要移除什么样式的legend。
2. 在相应的scale中移除，使用`guide=FALSE`选项。
3. 使用theme系统移除，使用`theme(legend.position="none")`


下面掩饰一张图使用不同命令的运行结果（图本身如文章开头所示）：

{% highlight r %}
p+guides(fill=FALSE)
{% endhightlight %}

{% highlight r %}
p+guides(color=FALSE)
{% endhightlight %}

{% highlight r %}
p+scale_color_brewer(guide=FALSE)
{% endhightlight %}

{% highlight r %}
p+theme(legend.position="none")
{% endhightlight %}

{% highlight r %}
p+theme(legend.position="top")
{% endhighlight %}

