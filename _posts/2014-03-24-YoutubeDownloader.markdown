---
author: Longqi
comments: true
date: 2014-03-24 16:26:16+00:00
layout: post
slug: Youtube-dl
title: 下载Youtube视频的利器
categories: [Tools]
tags:
- Python
---

有很多下载youtube视频的插件，不过一句话更新不够快，功能不够强。这个时候python出马瞬间秒杀一切。这一工具可以下载不止是youtube视频，什么搜狐、优酷等等都可以简单搞定。不支持的站点自己解析一下，添加一个parser就能搞定。

同时，程序支持下载youtube播放列表，真是无敌强悍啊！还可以提前音频，合并视频如此等等不胜枚举。

还有还有，更新速度超快，一两天一个版本，很少有失效的时候:-D。当然有多种细致选项应有尽有，强烈推荐啦！

神器大名youtube-dl，python写成，有编译好的exe。默认选项是下载最高清晰度的视频。常用的命令如下：


    youtube-dl.exe -U  更新程序
    youtube-dl.exe URL 下载URL 的视频


下载列表时有时需要更改URL，比如以下URL：[http://www.youtube.com/watch?v=Ucrs7DUCkr8&list=FLkhm72fuzkS9fYGlGpEmj7A]， 需要将v=Ucrs7DUCkr8&从URL删除，这样才能按照列表下载。

只需要下载部分列表内容时会使用到列表视频的编号

    --playlist-start NUMBER
    --playlist-end NUMBER

可以用来设置列表中开始下载的编号和结束的编号。

    youtube-dl.exe -F URL 可以用来查看下载的URL的视频可用的格式
    youtube-dl.exe -f NUMBER URL 可以用来下载制定格式的视频
    youtube-dl.exe -x URL 用来提取URL视频中的声音
    youtube-dl.exe -x -k URL 再提取URL声音之后保留视频本身


其他参数不很常用，需要了解时可以使用youtube-dl.exe -h查询即可。最后，youtube-dl的下载地址是：[http://rg3.github.io/youtube-dl/](http://rg3.github.io/youtube-dl/)。希望大家下载愉快！

