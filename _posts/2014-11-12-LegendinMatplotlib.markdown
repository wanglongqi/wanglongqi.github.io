---
author: Longqi
comments: true
date: 2014-11-12 11:29:13
layout: post
slug: LegendinMatplotlib
title: Matplotlib中Legend怎么设置到坐标轴外侧
categories: [Python]
tags:
- Matplotlib
- Python
- Tutorial
---
![](/public/images/Fig5.png)
Matplotlib的Legend和Matlab很像，但是没有选项可以直接将Legend放置到坐标轴外侧。默认的定位选项loc有以下选项：

	loc : int or string or pair of floats, default: 0
	    The location of the legend. Possible codes are:

	        ===============   =============
	        Location String   Location Code
	        ===============   =============
	        'best'            0
	        'upper right'     1
	        'upper left'      2
	        'lower left'      3
	        'lower right'     4
	        'right'           5
	        'center left'     6
	        'center right'    7
	        'lower center'    8
	        'upper center'    9
	        'center'          10
	        ===============   =============

    Alternatively can be a 2-tuple giving ``x, y`` of the lower-left
    corner of the legend in axes coordinates (in which case
    ``bbox_to_anchor`` will be ignored).

所以，结论是你要么把Legend放在坐标轴区域内，要么直接给定坐标。那么怎么把Legend放到坐标轴外呢，答案是没有直接的好办法，这里提供一个凑活能使的方案。需要用到Legend函数的一个选项：

	bbox_to_anchor : :class:`matplotlib.transforms.BboxBase` instance                          or tuple of floats
	    Specify any arbitrary location for the legend in `bbox_transform`
	    coordinates (default Axes coordinates).

	    For example, to put the legend's upper right hand corner in the
	    center of the axes the following keywords can be used::

	       loc='upper right', bbox_to_anchor=(0.5, 0.5)

用法并不复杂，设置一个Legend在bbox坐标下的位置，然后配合参数使用。什么是bbox呢？这个可以理解成坐标轴区域是(0,1)的一个坐标系。那么放在坐标轴外面就是大于1的值了。

看起来不错哦，不过直接放置到坐标轴之外也会直接放置到绘图区外了，所以需要先调整坐标轴在绘图区的位置，这也就是为什么说这个解决方案不那么理想的原因啦！那怎么调节坐标轴的大小呢？那只好去翻Axes的手册了，然后你可能会找到下面这个函数

	Definition:  ax.set_position(self, pos, which=u'both')
	Docstring:
	Set the axes position with::

	  pos = [left, bottom, width, height]

	in relative 0,1 coords, or *pos* can be a
	:class:`~matplotlib.transforms.Bbox`

这样这个工作就越来越像Matlab中的高级绘图控制了，很遗憾好像你必须那么做。

缩放好之后你就可以用`bbox_to_anchor`函数把Legend放置到需要的位置了。有点抽象啊，给个例子吧！

{% highlight python %}

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 10:27:22 2014

@author: longqi
"""

from pylab import *

x = arange(0,20,.3)
y = sin(x)

plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'])

{% endhighlight %}

![](/public/images/Fig1.png)

{% highlight python %}

figure()

plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],3)

{% endhighlight %}

![](/public/images/Fig2.png)

{% highlight python %}

figure()
plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],bbox_to_anchor=(0.5,0.5),loc=10)

{% endhighlight %}

![](/public/images/Fig3.png)

{% highlight python %}

figure()
plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],bbox_to_anchor=(1.02,0.8),loc='center left')

{% endhighlight %}

![](/public/images/Fig4.png)

{% highlight python %}

figure()
ax = gca()
ax.set_position([0,0,0.8,1])
plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],bbox_to_anchor=(1.02,0.8),loc='center left')

{% endhighlight %}

![](/public/images/Fig5.png)


代码中展示了一下plot函数中众多选项中的一部分，legend函数的其他有用选项比如可以这样控制legend的样式：

{% highlight python %}

figure()
plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],loc='best',fancybox=True,shadow=True,numpoints=1,)

{% endhighlight %}

![](/public/images/Fig7.png)

总之，Matplotlib用于2D绘图还是比较优秀的，图像的效果一般来讲和Matlab的图像有过之而无不及。不过有些功能却不太容易实现，还需要大家不断的探索解决方案。

