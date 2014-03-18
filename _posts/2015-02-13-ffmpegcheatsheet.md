---
author: Longqi
comments: true
date: 2015-02-13 13:18:45
layout: post
slug: ffmpegcheatsheet
title: ffmpeg的快速参考卡片
categories: [Tools]
tags:
- ffmpeg
- Documents
---
ffmpeg功能强大，选项复杂，大多数情况下根本顾不过来。对于一般运用来讲，情况并不很多，这里整理一部分常见的任务，以供使用时参考:

查看文件信息：

	ffmpeg -i INPUT

将图片转换为视频：（-r 是帧率，-s 是宽和高）
	
	ffmpeg -f image2 -i foo-%03d.jpeg -r 12 -s WxH foo.avi

将图片转换为视频：（-r 是帧率，-s 是宽和高）【这个用的是glob，不是文件序列】

	ffmpeg -f image2 -pattern_type glob -i 'foo-*.jpeg' -r 12 -s WxH foo.avi

将视频导出为图像：

	ffmpeg -i INPUT image%d.jpg

将视频转换为使用各种设备的文件可参见http://www.rodrigopolo.com/ffmpeg/cheats.php 的参数列表。

转换格式一般的选项是这样的：

	ffmpeg -i INPUT -b 比特率 -s 宽x高 -vcodec 视频编码器 -ar 音频采样率 -acodec 音频编码器 OUTPUT

这里简单的列一下常用的编解码器和选项：

-acodec 音频编码器
	copy
	直接拷贝
	mp2
	视频里偶尔用，MP2
	libmp3lame
	MP3
	pcm_u8 或者 pcm_u16
	8或者16位的wav
	vorbis
	ogg

-ab 音频编码率

	128k, 192k 什么的啦！

-aq 音频质量

	和VBR联用，是-q:a的别名。从0开始，与编码器相关，数值代表的意思参见编码器说明。

-ar 音频采样率

	单位Hz

-ac 声道数

	设置音频通道的数目。输出流默认将设置为输入音频信道的数目。

-vcodec 视频编码器
	copy
	直接拷贝
	flv
	flv的啦
	mpeg2
	mpg文件mpeg2编码
	mpeg4
	mpg文件mpeg4编码，能用这个别用上面那个
	msmpeg4v2
	默认.avi后缀

-codecs
	看看你机器上现有的视频编码器


其他的不写了，如果需要的话，参见手册。

