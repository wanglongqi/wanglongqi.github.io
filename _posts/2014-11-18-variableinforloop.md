---
author: Longqi
comments: true
date: 2014-11-18 13:13:14
layout: post
slug: VariableinForLoop
title: 批处理中for循环怎么去掉变量的后缀名
published: True
categories: [System]
tags:
- Windows
- System
- Batch
---
![cmd](/public/images/cmd.png)
在for循环中可以使用的变量名修改符包括：

    %~I         - 将 %I 去掉变量两边的双引号 (")
    %~fI        - 将 %I 转换到路径全称
    %~dI        - 将 %I 转换到盘符名
    %~pI        - 将 %I 转换到路径
    %~nI        - 将 %I 转换到文件名
    %~xI        - 将 %I 转换到后缀名
    %~sI        - 将 %I 转换到短路径名
    %~aI        - 将 %I 转换到文件属性
    %~tI        - 将 %I 转换到文件日期
    %~zI        - 将 %I 转换到文件大小
    %~$PATH:I   - 查找搜索路径并补全到 %I

这些选项可以叠加使用，例如：

    %~dpI       - 将 %I 转换到盘符名加路径
    %~nxI       - 将 %I 转换到文件名加扩展名

所以，用%~nI即可以去掉变量的后缀名，仅保留文件名。