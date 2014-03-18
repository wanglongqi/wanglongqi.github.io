---
author: Longqi
comments: true
date: 2014-11-17 14:02:46
layout: post
slug: ConvertSVG2PNG
title: 批量转换SVG为PNG
published: True
categories: [Inkscape]
tags:
- Inkscape
- Tutorial
---
![InkBatch](/public/images/inkbatch.png)
今天想把一组头像SVG转换成PNG文件，又不想打开Inkscape一个一个转换，所以就想用Inkscape的命令行接口，但是发现批量转换Inkscape真的好慢，每次都要启动关闭。网上搜了一下除了一个叫InkscapeBatch的程序，好像也没有什么靠谱的选项了。下载下来之后还和便携版不兼容，是可忍孰不可忍。那么简单的问题怎么要弄得那么复杂，不愧是程序猿啊！还是得自己动手丰衣足食啊！

原理很简单了，不让Inkscape每次都启动即可，这个很困难吗，当然不是Inkscape设计人员还是挺靠谱的。下面就是我的解决方案：

{% highlight batch %}
if exist input del input
for %%i in (*.svg) do @echo %%i -e %%~ni.png -w 500 >> input
echo quit >> input
inkscape.com --shell <input
{% endhighlight %}

是不是很简单啊！如果想要搞清楚这些参数的含义可以参考其他几篇文章哦：[Inkscape的命令行参数]({% post_url 2014-11-17-inkscapecommandline %})和[批处理中for循环怎么去掉变量的后缀名]({% post_url 2014-11-18-variableinforloop %})。

也可以新建一个命令svg2png。内容如下即可：

{% highlight batch %}
if exist input del input
for %%i in (%*) do @echo %%i -e %%~ni.png>> input
echo quit >> input
inkscape.com  --shell <input
{% endhighlight %}

类似的可以有svg2eps。

{% highlight batch %}
if exist input del input
for %%i in (%*) do @echo %%i -E %%~ni.eps>> input
echo quit >> input
inkscape.com  --shell <input
{% endhighlight %}

