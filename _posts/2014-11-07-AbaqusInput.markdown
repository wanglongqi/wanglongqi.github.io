---
author: Longqi
comments: true
date: 2014-11-07 23:30:41
layout: post
slug: AbaqusInput
title: Abaqus Input文件的语法规则
categories: [Abaqus]
tags:
- Abaqus
- Tutorial
---
![Abaqus Related Post](/public/images/abaqus.png)
Abaqus Input文件是Abaqus计算使用的实际输入文件，该文件有三种类型的语句：

1. 关键字语句：
	- 第一个非空白字符必须是星号（*）；
	- 可以带参数，参数用逗号隔开；
	- 空白符默认被忽略；
	- 大小写无关；
	- 不能长于256字符；
	- 关键字和参数都可以*部分*输入，只要能够唯一确定即可；
	- 若参数需要给值，用=给定；
	- 其他不常用约定，参见文档1.2.1。
2. 数据语句：经常紧接在关键字行以后（不能随意加空行）
	- 数据逗号隔开；
	- 不要长于256字符；
	- 整数参数*不能超过9位*；
	- 数据语句中可以出现*集合*；
	- 其他参见文档1.2.1。
3. 注释语句：行起始两个字符均为星号，也即“**”


嗯，这个就是Abaqus Input 文件的主要语法了。很简单吧，总的来讲Abaqus Input文件是一个设计相对简单的格式文件，读取也相对容易。不过这不妨碍Abaqus拥有大量的关键字，使得整个Abaqus的功能很强大，掌握也不容易。Abaqus的Keywords手册都是上千页的。这也算是计算机程序的魅力之一吧，简单的规则总是可以表现复杂的事物。
