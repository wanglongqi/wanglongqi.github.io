---
author: Longqi
comments: true
date: 2015-06-01 21:56:48
layout: post
slug: colorbrewerrelease
title: ColorBrewer in Mathematica
categories: [Mathematica]
tags:
- Mathematica
---
![ColorBrewer](/public/images/colorbrewer.png)
也算是Mathematica的老用户了，看过Core Language的帮助，很庞杂，不过设计很统一，可以很容易的表达很复杂的想法。但是，一直都局限于简单地符号运算，没有太多的深入。会用的功能基本也就是其他函数式程序语言中已经学会的那些概念，并没有过多的钻研。

最近在用Mathematica做一些公式推导，顺便做一些绘图，认真用一下之后发现对于解析表达式的绘图，Mathematica可以轻易的超过其他绘图软件，因为它利用了它绘制的内容是是函数，而不是仅仅的数据。这样通过一些相信并不简单地算法，可以用数量有限的点反应出函数的趋势。这是一般的绘图软件很难做到的，稍后有时间会单开一个文章谈谈Mathematica里面的自适应采样算法。

用惯了ColorBrewer的配色方案，而Mathematica里没有现成的支持。所以最好的办法就是自己做一个了，因此就写了一个ColorBrewer的包，用于支持Mathematica中使用ColorBrewer的需求。具体的情况可以参见[项目的主页](https://github.com/wanglongqi/ColorBrewer)，这里就不过多介绍了。

程序包可以生成Palette，也可以生成ColorFunction，还可以显示Palette（这个是我感觉比其他ColorBrewer库方便的地方，Mathematica里可以直接看到Palette的颜色，直接从里面直观的选取。其他语言的库都很难提供类似的功能，即使提供了也没有Mathematica那么统一的显示和使用方法。）

![Palette](/public/images/display.png)
![Palette](/public/images/div.png)
