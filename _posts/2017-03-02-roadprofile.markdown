---
author: Longqi
comments: true
date: 2017-03-02 21:19:16 +0800
layout: post
slug: dplyrpar
title: 路面粗糙度的模拟
categories: [Python]
tags:
-  Research
-  Python
-  Share
---
最近弄一些和路面粗糙度相关的东西，想用粗糙度来进行一些数值仿真，找了半天都没有找到合适好用的代码，不是太复杂，就是各种运行不成功。索性自己写一个吧，描述的路面粗糙度的标准是ISO 8608，对应的欧标是BS 7853。标准里没有给具体的实现方法，只有空间谱的大小。所以查找了一下文献，发现了下面这篇文献定义了一个直接使用ISO 8608给出的路面谱的方法：

    Da Silva, J. G. S. "Dynamical performance of highway bridge
    decks with irregular pavement surface."
    Computers & structures 82.11 (2004): 871-881.

算法不复杂，整个实现也就几十行代码，可以到[这里查看](https://github.com/wanglongqi/RoadProfile/blob/master/roadprofile.py)。

算出来的结果和标准是可以吻合的：

![PSD](https://github.com/wanglongqi/RoadProfile/blob/master/example/example1.png?raw=true)

有相关需求的读者欢迎围观，欢迎指正。

