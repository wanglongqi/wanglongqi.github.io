---
author: Longqi
comments: true
date: 2014-11-19 13:34:55
layout: post
slug: StopDocear4word
title: 暂时不要使用Docear4Word (Do not use Docear4Word now.)
published: True
categories: [Tools]
tags:
- BibTeX
- Word Integration
- Winodws
---
![Docear](/public/images/reftools.png)
Docear是一套文献管理软件，之前有同学推荐我用，不过一直不得要领也就没有继续使用。不过发现Docear网站上的Docear4Word软件做得很小巧，功能也比较符合联合BibTeX使用，所以也就一直在使用。以前也出现过一些问题不过由于一篇文章也就二三十篇参考文献手动调整一下也就算了。最近在写开题报告，参考文献已经过百，发现Docear4Word在很多期刊的格式渲染上有问题。

比如，使用IEEE格式渲染数据库文件的结果是：

	[1]	M.-B. Abdo and M. Hori, “A numerical study of structural damage detection using changes in the rotation of mode shapes,” Journal of Sound and vibration, vol. 251, no. 2, pp. 227–239, 2002.
	[2]	H. Ahmadian and H. Jalali, “Generic element formulation for modelling bolted lap joints,” Mechanical Systems and Signal Processing, vol. 21, no. 5, pp. 2318–2334, 2007.
	[3]	J. Esteban and C. A. Rogers, “Energy dissipation through joints: theory and experiments,” Computers & Structures, vol. 75, no. 4, pp. 347–359, 2000.
	[4]	W. Fan and P. Qiao, “Vibration-based damage identification methods: a review and comparative study,” Structural Health Monitoring, vol. 10, no. 1, pp. 83–111, 2011.

但是用Elsevier格式渲染出来的结果是这样的：

	[1]	M.-B. Abdo, M. Hori, A numerical study of structural damage detection using changes in the rotation of mode shapes, Journal SoundVibration. 251 (2002) 227–239. http://www.sciencedirect.com/science/article/pii/S0022460X01939896.
	[2]	H. Ahmadian, H. Jalali, Generic element formulation for modelling bolted lap joints, MechanicalSystems Signal Processing. 21 (2007) 2318–2334. http://www.sciencedirect.com/science/article/pii/S0888327006002263.
	[3]	J. Esteban, C.A. Rogers, Energy dissipation through joints: theory and experiments, Computers&Structures. 75 (2000) 347–359. http://www.sciencedirect.com/science/article/pii/S0045794999000966.
	[4]	W. Fan, P. Qiao, Vibration-based damage identification methods: a review and comparative study, StructuralHealthMonitoring. 10 (2011) 83–111.

Elsevier格式的渲染所有的期刊名都是不对的，而且还有其他人半年前就报告[其他类似Bug](http://www.docear.org/support/forums/docear-support-forums-group3/bug-reports-forum6/docear4word-styles-from-csl-site-not-working-thread895/)，官方已经接受了报告，但是半年都没有推出修正，这样的速度是不能够接受的。因此，建议大家使用其他的Bibtex与Word的接口程序，比如[Mendeley](http://www.mendeley.com)或者[Zotero](http://zotero.org)或者[Papers](http://www.papersapp.com)。不过我都没有尝试过，不单独推荐某个软件。对于Mendeley和Zotero，第一感觉是更多的像文献管理软件，而不是BibTeX集成的解决方案。个人比较喜欢用JabRef，Mendeley的界面看着也不错，使用起来和Docear4Word比较类似，试用了一下感觉很不错。由于之前有同学报告过Mendeley有一些问题，我需要在使用一段时间才能有结论，之后再报告啦！


