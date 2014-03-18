---
author: Longqi
comments: true
date: 2015-06-04 09:15:03
layout: post
slug: writetexmac
title: A short note about WriteTeX on MAC OSX
categories: [Inkscape]
tags:
- Inkscape
- WriteTeX
---
![macwritetex](/public/images/macwritetex.png)
I have waited for `pdf2svg` or `pstoedit` to release a binary version for MAC OSX for a very long time until yesterday I was so disappointed and tried to solve it myself. I finally figured out a way to use `WriteTeX` in MAC OSX without `fink` installed. <del> I upload a binary version of pstoedit for Mac OSX binary into the repository of `WriteTeX`, which is depending on [Inkscape of this version]({% post_url 2014-11-04-InksacapeNative %}) installed in default location (Drag the app into your `Applications` folder). If you have no problem with these settings and you have the administrator privilege, then here is a solution for you.</del>

1. <del>Download the binary from [https://github.com/wanglongqi/WriteTeX/raw/master/pstoedit.zip](https://github.com/wanglongqi/WriteTeX/raw/master/pstoedit.zip) and unzip it.</del>
2. <del>Copy all the files to /usr/bin</del>
3. <del>Copy WriteTeX plugin to `/Applications/Inkscape.app/Contents/Resources/share/inkscape/extensions`</del>
4. <del>Start Inkscape to use WriteTeX</del>

<del>Hope you like it!</del>

## Good news
I complied a standalone binary `pstoedit`, please download the binary from [the repository](https://github.com/wanglongqi/WriteTeX/raw/master/pstoedit.zip) and put into executable path. For more details, please read the post [here]({% post_url 2015-06-12-pstoeditbinary %}).

