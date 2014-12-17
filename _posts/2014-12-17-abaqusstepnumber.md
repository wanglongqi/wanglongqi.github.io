---
author: Longqi
comments: true
date: 2014-12-17 21:44:47
layout: post
slug: abaqusstepnumber
title: Abaqus的载荷步是怎么编号的？
categories: [Abaqus]
tags:
- Abaqus
- Tutorial
---
![Abaqus Related Post](/public/images/abaqus.png)
添加预应力场的时候需要填入读取ODB文件的载荷步和增量步，那么问题是载荷步和增量步是怎么算的呢？初始步后面是那一步是第二步还是第一步？增量步的初始步算第一步吗？

答案是：初始步是第0步，初始步也是第0步。因此，初始步后那一步是第一个载荷步，增量初始步后第一个增量步是第一个增量步。

