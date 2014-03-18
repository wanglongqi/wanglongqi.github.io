---
author: Longqi
comments: true
date: 2014-11-21 10:24:27
layout: post
slug: UnevenSpectrum
title: 非定间隔采样的功率谱估计
categories: [SignalProcessing]
tags:
- SignalProcessing
- Scipy
---
![Python Related Post](/public/images/python.png)
定间隔采样的功率谱估计方法多入牛毛，那么不定间隔采样信号的功率谱应该怎么计算呢？

个人觉得基于重采样的思路是一条可行的道路，然后就是直接估计啦！Scipy中提供了一种基于最小二乘的直接估计方法：Lomb-Scargle periodogram。算法的效率是$O(n^2)$，对于这个问题还是比较可以接受的。

详细用法可以参见`scipy.signal.lombscargle`的帮助文档，文档写得很细致，同时还给出了参考文献。大致翻译一下文档介绍部分：

	scipy.signal.lombscargle(x, y, freqs)
	计算Lomb-Scargle周期图.

	计算得到的周期图没有归一化，放大系数为(A**2) * N/4 ，A是对于足够大N的正弦信号的幅值。

	参数:	
	x : 数组
	采样时间
	y : 数组
	测量值
	freqs : 数组
	输出周期图的角频率
	返回值:	
	pgram : 数组
	Lomb-Scargle周期图

归一化那个看不懂的，可以参见文档里的例子。

