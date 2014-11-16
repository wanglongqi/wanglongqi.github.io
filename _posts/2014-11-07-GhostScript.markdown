---
author: Longqi
comments: true
date: 2014-11-07 12:25:01
layout: post
slug: GhostScript
title: GS (GhostScript)的快速参考卡片
categories: [Tools]
tags:
- GS
- CheatSheet
- Forward
---
![GhostScript Logo](/public/images/gs.svg)
GhostScript是处理PDF和PS的神器，但是实在太难用了。今天看到一个[不错的总结](http://flukylogs.blogspot.sg/2012/08/gs-ghostscript-cheat-sheet.html)转载并翻译修改一下：

- PS到PDF:

		gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=fileout.pdf filein.ps 

- 合并多个PS或者PDF到一个文件:

		gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=fileout.pdf filein1.ps filein2.pdf filein3.pdf

- 从PS或者PDF中提取若干页:

		gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dFirstPage=3 -dLastPage=3 -sOutputFile=fileout.pdf filein.ps

- 在PDF中嵌入字体（-dEmbedAllFonts=true -dSubsetFonts=true联用可以减小尺寸）:

		gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=fileout.pdf  -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -dSubsetFonts=true -dCompatibilityLevel=1.6 filein.pdf

- 从PDF中去除大部分内嵌字体:

		gs -q -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=fileout.pdf  -dPDFSETTINGS=/prepress -dEmbedAllFonts=false -dCompatibilityLevel=1.6 filein.pdf

- 转换图像到PDF:

		最好使用ImageMagic的convert命令
		convert *.png out.pdf
		convert -compress jpeg *.png out.pdf

- GS里的默认配置文件

		-dPDFSETTINGS=/screen (screen-view-only quality, 72 dpi images)
		-dPDFSETTINGS=/ebook (low quality, 150 dpi images)
		-dPDFSETTINGS=/printer (high quality, 300 dpi images)
		-dPDFSETTINGS=/prepress (high quality, color preserving, 300 dpi imgs)
		-dPDFSETTINGS=/default (almost identical to /screen)

- GS里的纸张大小设置

		Paper size options
		-sPAPERSIZE=letter
		-sPAPERSIZE=a4
		-dDEVICEWIDTHPOINTS=w -dDEVICEHEIGHTPOINTS=h (point=1/72 of an inch)
		-dFIXEDMEDIA (force paper size over the PostScript defined size)
		-gWIDTHxHEIGHT  (page size in pixels)

- GS里可用的设备名称

		-sDEVICE=pdfwrite
		-sDEVICE=ps2write
		-sDEVICE=png16m  (24-bit RGB color)
		-sDEVICE=pnggray  (grayscale)
		-sDEVICE=pngmono  (black-and-white)
		-sDEVICE=pngalpha (32-bit RGBA color)
		-sDEVICE=jpeg   (color JPEG)
		-sDEVICE=jpeggray  (grayscale JPEG)
		-sDEVICE=epswrite  (encapsulated postscript)
		-sDEVICE=txtwrite  (text output, UTF-8)

如果需要输出多页需要在-sOutputFile中设置文件名模板，参见下面的示例。

- 列出可用的设备和相应文档: 

		gs -h

- 其他有用的选项

		-dNOPAUSE    不会每页都停一下
		-dBATCH  跑完就退出了
		-sOutputFile=ABC-%03d.pgm (produces 'ABC-001.pgm'..'ABC-010.pgm'..) 这个就是多页的模板
		-dEmbedAllFonts=true
		-dSubsetFonts=true  仅嵌入部分字体
		-dCompatibilityLevel=1.4  (Adobe's PDF specifications,
		                           >=1.4 for font embedding,  （支持嵌入字体）
		                           =1.6 for OpenType font embedding) （支持OpenType字体嵌入）
		-dCompressPages=true  (compress page content) 压缩页面内容
		-dFirstPage=pagenumber
		-dLastPage=pagenumber
		-dAutoRotatePages=/PageByPage  (or /All or /None)
		-rXRESxYRES (XRES & YRES in pixels/inch) 文件纵横分辨率
		-rRES (same XRES & YRES, affects images and fonts converted to bitmaps)
		-sPDFPassword=password

- PDF切边（使用pdfcrop，gs可以做，不过好像不一定好用）

		pdfcrop in.pdf out.pdf  (一般这一句就够了，pdfcrop --margins ’左 上 右 下’ input.pdf output.pdf  可以来设置边距)
		gs -sDEVICE=pdfwrite -dBATCH -dNOPAUSE -dQUIET -sPAPERSIZE=a4 -dPDFFitPage -sOutputFile=resized.pdf cropped.pdf （这个是用来调整页面大小的，-dPDFFitPage会缩放PDF页面，而不是直接将页面填白到指定大小）

非要用GS切边的可以参考这个，不一定好用

	gs -sDEVICE=bbox -dNOPAUSE -dBATCH file.pdf    找出页面大小
	gs -sDEVICE=pdfwrite \
		   -o trimmedFile.pdf \
		   -c "[/CropBox [这个是页面大小，四个数字在这] /PAGES pdfmark" \
		   -f file.pdf

- 生成PDF/A 或者PDF/X

		gs -dPDFA=1 -dBATCH -dNOPAUSE -dNOOUTERSAVE -sColorConversionStrategy=/RGB -sOutputICCProfile=srgb.icc -sDEVICE=pdfwrite -sOutputFile=out-a.pdf PDFA_def.ps input.ps

		gs -dPDFA=2 -dBATCH -dNOPAUSE -dNOOUTERSAVE -sColorConversionStrategy=/RGB -sOutputICCProfile=srgb.icc -sDEVICE=pdfwrite -sOutputFile=out-a.pdf PDFA_def.ps input.ps

		gs -dPDFX -dBATCH -dNOPAUSE -dNOOUTERSAVE -sColorConverionStrategy=/CMYK -sOutputICCProfile="ISO Coated sb.icc" -sDEVICE=pdfwrite -sOutputFile=out-x3.pdf PDFX_def.ps input.ps

还有很多选项，这次就列那么多吧，需要的用到的时候再更新这个页面。