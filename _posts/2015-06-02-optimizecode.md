---
author: Longqi
comments: true
date: 2015-06-02 18:20:00
layout: post
slug: colorbrewerrelease
title: 优化表达式：Mathematica vs. Maple
categories: [Mathematica]
tags:
- Mathematica
- Maple
---

表达式优化一般是将符号运算解输入到程序的最后一步，Maple和Mathematica都提供了相似的功能。对于Maple，这个功能有CodeGeneration函数包提供，可以转换为Matlab，Python，C，Fortran等等格式的代码。例如：

	e=(x+2*y)^2+sin(x+2*y)+sin(x)^3
	Matlab(e, optimize = true);

	t2 = x + 2 * y;
	t3 = t2 ^ 2;
	t4 = sin(t2);
	t5 = sin(x);
	t6 = t5 ^ 2;
	t8 = t6 * t5 + t3 + t4;

对于Mathematica问题稍微复杂一点，因为需要用到一个没有文档的函数，格式是这样的：

	?? Experimental`OptimizeExpression

	Experimental`OptimizeExpression

	Attributes[Experimental`OptimizeExpression]={Protected}
	 
	Options[Experimental`OptimizeExpression]={ExcludedForms->{},ExternalForms->{},InertForms->{},OptimizationLevel->1,OptimizationSymbol->Compile`$}

结果是差不多的：

	In:= e = (x + 2 y)^2 + Sin[2 y + x] + Sin[x]^3

	Out= (x + 2 y)^2 + Sin[x]^3 + Sin[x + 2 y]

	In:= Experimental`OptimizeExpression[e, OptimizationLevel -> 2, 
	 OptimizationSymbol -> C]

	Out= Experimental`OptimizedExpression[
	 Block[{C3, C4, C5, C6, C7, C8}, 
	 C3 = 2 y; 
	 C4 = x + C3; 
	 C5 = C4^2; 
	 C6 = Sin[x]; 
	 C7 = C6^2; 
	 C8 = C6 C7; 
	 C5 + C8 + Sin[C4]]]

不能不说Maple在这方面的支持确实比Mathematica方便一些，而且能够输出多种语言的代码。另外提一句，Maple可以导出的函数数量远远大于Mathematica，比如Maple可以导出贝塞尔曲线的拟合结果成各种程序代码，而Mathematica目前还没有支持。
