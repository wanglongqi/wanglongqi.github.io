---
author: Longqi
comments: true
date: 2015-02-02 17:09:56
layout: post
slug: colorcycle
title: 替换默认的Matplotlib的颜色循环
published: True
categories: [Python]
tags:
- Matplotlib
- Python
---
![Python](/public/images/colorcyc.png)
先前Matplotlib为了模拟Matlab，把默认的颜色循环改成和Matlab默认的一致，真是丑爆了。最近Matlab也把自己的颜色循环改了，相信Matplotlib很快也会改吧。不过，你也可以不用等到默认的颜色循环修改了，直接用`cm`模块里的色板就好了。方法是这样的（这里设置为7色的Set3色板）：

{% highlight python %}
from pylab import cm
rcParams['axes.color_cycle']=list(cm.Set3(linspace(0,1,7)))
{% endhighlight %}

然后绘制一下线图，就能获得文章开头的那个颜色循环了。是不是比默认的颜色循环好的了。

