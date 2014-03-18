---
author: Longqi
comments: true
date: 2014-11-23 20:17:07
layout: post
slug: MirrorSite
title: 国内镜像站点
published: True
categories: [Site]
tags:
- Site
---
国内访问Github的速度好像不怎么好，而且随时有访问不了的可能性。所以在国内的Github模仿站Gitcafe上建了一个[镜像站点](http://whyhow.gitcafe.com)，同时更换了网站主题。

说起这个事情也很感慨啊，开始的时候在Blogger上做博客，花了不少经历。但是后来Blogger被封了，也就放弃了。之后尝试过百度的空间，和一些小的免费空间，都不很好用。最长的一个应该算gofreeserve上的那个wordpress站点，但是越来越坚持不下去，先是gofreeserve自己当机，后来在国内被封锁了，然后干脆解析不了。最后，现在连登录都登录不上了。再往后就是百度上面的托管网站了，本来觉得百度是个大公司，应该不会坑人吧，结果BAE升级，然后学校封锁BAE，然后BAE推出收费加实名认证。现在网站已经不能访问了。

再往后就是Github的站点了，应该Github在国内封锁过一次，之后有解封了。所以有可能短期内不会封锁，不过等到国内站点翅膀硬了，封锁也不是不可能的。先托管在Github吧，镜像站点也试了国内的几个，以防Github被封，看大多数人推荐GitCafe。一方面Gitcafe是国产版的Github，如果Github被封，Gitcafe很有可能成为其国内替代，所以镜像在Gitcafe上应该是可靠的；另一方面，Gitcafe据传国内访问速度很快，这样对于中文为主体的网站还是吸引力不小。所以，最后选择了Gitcafe作为镜像站点的托管网站。

不过，这个镜像站点也不是完全的镜像啦！我开始也考虑直接用同一个git库，push到两个remote就行了。后来还是觉得单独弄两个Git库更好一些，一方面一些文件没有必要在两个库里都保存（比如CHM文件，体积很大，放到Gitcafe有点浪费人家的空间）；另外一方面也想脱离开页面和Github项目的关系，希望在Github的页面上有自己Github的项目的源码，但是在Gitcafe上不希望外链到Github的项目上来；再一方面也是想尝试一下新的模板，这样可以把一些相对实验性的东西先放到镜像站上，觉得不错了在挂到Github上来。


