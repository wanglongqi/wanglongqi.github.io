---
author: Longqi
comments: true
date: 2014-11-10 00:09:12
layout: post
slug: WeChatVideo
title: 你知道微信小视频是有声的吗？
categories: [Opinion]
tags:
- WeChat
- Tencent
---
![wechat](/public/images/wechat.png)
自从微信6.0开始，微信号称进入了小视频时代了。刚开始的时候认为小视频嘛，肯定是有声音有图像，就是把视频文件发上去。结果使用之后发现好像只有图像没有声音，感觉就像是动态gif。好吧，我承认我也被忽悠过去了，而且还吐槽了一番前一久不是刚说H.264的压缩能力已经超越了gif，想小视频这样的动画完全应该用H.264来做嘛。

万万没想到啊，腾讯这次真用的是H.264啊！而且是记录了声音和图像的H.264啊！那为什么腾讯只给看图像不给放声音，让我好久都认为那是个动态gif，或者至少是没有录制声音的视频文件。我为什么知道呢？因为我把文件拷出来了，下面是其中一个文件的播放记录：

	libavformat file format detected.
	[lavf] stream 0: audio (aac), -aid 0, -alang und
	[lavf] stream 1: video (h264), -vid 0
	VIDEO:  [462H]  320x240  24bpp  24.000 fps  407.2 kbps (49.7 kbyte/s)
	Clip info:
	 major_brand: mp42
	 minor_version: 0
	 compatible_brands: mp42isom
	 creation_time: 2014-10-28 09:59:08
	==========================================================================
	Opening video decoder: [ffmpeg] FFmpeg's libavcodec codec family
	Selected video codec: [ffh264] vfm: ffmpeg (FFmpeg H.264)
	==========================================================================
	==========================================================================
	Opening audio decoder: [ffmpeg] FFmpeg/libavcodec audio decoders
	AUDIO: 16000 Hz, 1 ch, s16le, 32.5 kbit/12.71% (ratio: 4067->32000)
	Selected audio codec: [ffaac] afm: ffmpeg (FFmpeg AAC (MPEG-2/MPEG-4 Audio))
	==========================================================================
	AO: [coreaudio] 16000Hz 1ch s16le (2 bytes per sample)
	Starting playback...

小视频啊，图像是320x240  24.000 fps 407.2 kbps 的，声音是单声道的16000 Hz, 1 ch, s16le, 32.5 kbit。亲们，下次录制小视频的时候要注意自己在说什么了，不然会被录下来哦！

更新：有同学跟我说，你点开小视频之后打开放就能听到声音。好吧，我败给你了，你要**点开看**才有声音，那你还直接预览动画干什么？你点开看会有声音你不能给个提示吗？哎呀，看来我已经完全跟不上腾讯设计UI的理念了，老了，out了！
