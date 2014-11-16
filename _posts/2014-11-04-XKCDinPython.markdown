---
author: Longqi
comments: true
date: 2014-11-04 08:28:02
layout: post
slug: XKCDinPython
title: 怎么在Python里绘制XKCD风格的图像？
categories: [Python]
tags:
- Python
- Tutorial
---
![xkcd.png](https://wanglongqi.github.io/public/images/xkcd.png)
XKCD图片一直挺流行的，在很多软件中都可以实现，基本的想法都是原始图片加粗线条加抖动家卡通字体。Matplotlib也跟风开发了一个XKCD的绘制函数，效果还不错。官方推荐使用Humor Sans字体，可以去网上弄一个，不过没有的效果也不错。

这里画一个正弦曲线：

{% highlight python %}
from pylab import *
with xkcd():
    figure()
    x=arange(0,10,.01)
    y=sin(x)
    plot(x,y,x,cos(x),lw=3)
    xlabel('This is the x axis')
    ylabel('Ha, y axis')
    legend(['y=sin(x) curve','This is cos(x)?'])
    text(5,0,'I like this blog!')
    title('Why do people want xkcd? How to draw my own?')
show()    
{% endhighlight %}

然后你就得到了文章开头那张XKCD风格的图片了。当然，这个图片可以放到Inkscape里进行继续的修饰，直到你满意为止。

![xkcd.svg](https://wanglongqi.github.io/public/images/xkcd.svg)

