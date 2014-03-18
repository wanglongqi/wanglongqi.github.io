---
author: Longqi
comments: true
date: 2014-12-17 22:50:22
layout: post
slug: initialconditioninfreq
title: Abaqus频率提取步考虑预应力吗？
categories: [Abaqus]
tags:
- Abaqus
- Tutorial
---
![Abaqus Related Post](/public/images/abaqus.png)
Abaqus频率分析步到底受不受之前分析步的状态的影响呢？预应力会不会在计算中考虑到呢？

答案是一般来讲会的，但是需要注意，频率分析步是一个线性摄动步，不是动力学积分过程。以下是帮助文件中提及的相关内容：

- 如果频率提取步是计算的第一个载荷步，初始步的初始条件确定了系统的基本状态（预应力除外，第一步中，预应力不能作为频率提取步的初始条件。）否则，系统的基本状态是模型在上一个general分析步的最后增量步的状态。

- 预应力刚化效应只在频率提取步钱的general分析步打开了几何非线性的情况下有效。

原始帮助文件如下：

	Initial conditions


	If the frequency extraction procedure is the first step in an analysis, the initial conditions form the base state for the procedure (except for initial stresses, which cannot be included in the frequency extraction if it is the first step). Otherwise, the base state is **the current state of the model at the end of the last general analysis step** (“General and linear perturbation procedures,”  Section 6.1.3). Initial stress stiffness effects (specified either through defining initial stresses or through loading in a general analysis step) will be included in the eigenvalue extraction only if geometric nonlinearity is considered in a general analysis procedure prior to the frequency extraction procedure.

	If initial stresses must be included in the frequency extraction and there is not a general nonlinear step prior to the frequency extraction step, a “dummy” static step—which includes geometric nonlinearity and which maintains the initial stresses with appropriate boundary conditions and loads—must be included before the frequency extraction step.

