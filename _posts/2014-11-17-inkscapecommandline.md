---
author: Longqi
comments: true
date: 2014-11-17 16:50:40
layout: post
slug: InkscapeCommandLine
title: Inkscape的命令行参数
published: True
categories: [Inkscape]
tags:
- Inkscape
- Tutorial
---
![InkBatch](/public/images/inkscape.png)
Inkscape的命令行参数很多， 官网上有详细介绍，在这里做个简单的介绍。在Windows下为了确保可以启动命令行接口最好使用inkscape.com程序而不是inkscape.exe。

	## 命令格式

	inkscape [选项] [文件名 ...]

	## 常用选项

	    -V, --version
	    -e, --export-png=FILENAME				导出PNG的选项 
	    -a, --export-area=x0:y0:x1:y1  			导出一个区域的选项   
	    -C, --export-area-page
	    -D, --export-area-drawing
	        --export-area-snap
	    -i, --export-id=ID     
	    -j, --export-id-only     
	    -t, --export-use-hints
	    -b, --export-background=COLOR      		导出图片的背景
	    -y, --export-background-opacity=VALUE   导出图片的透明度
	    -d, --export-dpi=DPI              		导出图片的DPI
	    -w, --export-width=WIDTH          		导出图片的宽度
	    -h, --export-height=HEIGHT  			导出图片的高度
	    -P, --export-ps=FILENAME 				导出PS的选项 
	    -E, --export-eps=FILENAME 				导出EPS的选项 
	    -A, --export-pdf=FILENAME 				导出PDF的选项 
	        --export-latex
	    -T, --export-text-to-path
	        --export-ignore-filters
	    -l, --export-plain-svg=FILENAME
	    -p, --print=PRINTER 					使用打印导出文件的选项 
	    -I, --query-id=ID     
	    -X, --query-x
	    -Y, --query-y
	    -W, --query-width
	    -H, --query-height
	    -S, --query-all							查询信息的选项 
	    -x, --extension-directory
	        --verb-list
	        --verb=VERB-ID
	        --select=OBJECT-ID
	        --shell
	    -g, --with-gui                    
	    -z, --without-gui
	        --vacuum-defs
	        --g-fatal-warnings


带翻译的选项比较常用一些，如果需要协同其他程序使用其他选项也很有用。特别是对处理SVG文件的程序。下面是官方给出的命令行的使用范例：

{% highlight batch %}

打开文件
    inkscape filename.svg

从命令行打印
    inkscape filename.svg -p '| lpr'

导出SVG到90dpi的PNG
    inkscape filename.svg --export-png=filename.png

导出SVG到600*400的PNG
    inkscape filename.svg --export-png=filename.png -w600 -h400

导出SVG内所有对象的区域到PNG
    inkscape filename.svg --export-png=filename.png --export-area-drawing

导出SVG中id="text1555"的对象到PNG
    inkscape filename.svg --export-id=text1555 --export-use-hints

同上，但使用默认DPI,自定义文件名并调整导出区域至整数
    inkscape filename.svg --export-id=text1555 --export-png=text.png --export-area-snap

导出SVG到无Inkscape标签的SVG
    inkscape filename1.svg --export-plain-svg=filename2.svg

导出SVG到EPS，并将文字转换为路径
    inkscape filename.svg --export-eps=filename.eps --export-text-to-path

查询text1555的宽度
    inkscape filename.svg --query-width --query-id text1555

拷贝对象id="path1555"，并旋转90度，然后保存并退出。
    inkscape filename.svg --select=path1555 --verb=EditDuplicate --verb=ObjectRotate90 --verb=FileSave --verb=FileClose
{% endhighlight %}


感觉这个介绍已经很全面了，特别是对于一般用户。详细的解释可以参见帮助页面。
