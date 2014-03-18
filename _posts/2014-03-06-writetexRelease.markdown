---
author: Longqi
comments: true
date: 2014-03-06 16:08:55+00:00
layout: post
slug: writetex
title: WriteTeX：Inkscape的Tex插件
categories: [Inkscape]
tags:
- Inkscape
- WriteTeX
---

Inkscape以前一直不支持数学公式，后来有人想各种办法支持Latex。有很多很好的插件可以选择，但是大部分这些插件都是一次性的，输入之后就不能更改。textext是一个划时代的插件，它效果很好，而且支持修改，但是唯一的弱点是需要TK或者PyGtk的支持，为此经常要修正路径。它的作者是个Linux用户，对于Windows的支持并不很感冒。总之就是textext很好，但是还不完美，特别是对Windows的支持总有各种问题。更重要的原因是textext的作者已经很长时间没有更新textext了，代码里面很多BUG都没有修正。因此，我想开发一个新的Inkscape的Tex插件，当然textext提供了主要的思路。


开始想象中这个插件会很容易完成，稍微改动一下textext，直接提取代码，去掉GUI，用原生的扩展系统写一下应该就可以搞定。但是，如果textext的功能可以在原生的扩展系统中完成原作者怎么可能不直接做呢？问题在我开始动手写WriteTeX的时候就暴露出来，Inkscape的扩展系统的默认值是不可在程序中修改的，更可怕的是它会记住你的上一次输入。所以，textext的作者放弃了这个方案。一时间，我也觉得没有任何出路了。正在这个时候，错误对话框进入了我的视线，我也想起曾经replace_font插件使用错误对话框提示svg中使用的字体列表。因此，我开始构思使用错误对话框作为显示老的Tex代码的工具，虽然不如textext来得直接，但是总算也是提供了查看之前Tex代码的功能。从一定意义上这样也可以算部分的实现了可以修改之前Tex代码的需求，虽然还是不完美，不过我觉得是个不错的选择。因此，我们就有了WriteTeX。




经过两天断断续续的代码工作，第一个版本的WriteTeX出炉了，很不完美，差textext很远，主要的原因是我使用了很粗鲁的SVG合并的方式，直接将PDF到SVG转换的结果贴到了当前的SVG里，transform和style都没有处理。（这方面textext也有一些没有彻底完成）当然，很多textext中好的SVG的转换代码没有移植过来，很可惜！我会不断消化textext的处理方法，再添加到WriteTeX中来。不过不管怎么讲，这是一个可以工作的版本了，后面的工作主要是优化SVG合并的效果和ScaleFactor的工作模式。前面一项是插件的核心工作，但是我对SVG的标准不熟悉，还希望有人能够改善这部分代码。
