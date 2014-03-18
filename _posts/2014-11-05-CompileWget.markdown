---
author: Longqi
comments: true
date: 2014-11-05 15:02:41
layout: post
slug: ComplieWget
title: Mac下编译wget
categories: [System]
tags:
- Mac
- wget
- Software
---
![Mac OSX Related Posts](/public/images/macosx.png)
上周wget爆出了一个大的[安全漏洞](http://www.freebuf.com/vuls/49641.html)，安全漏洞波及1.14以前的wget版本。今天查了一下机器上的wget是1.14，所以考虑更新一下，但是有忘了怎么编译了。重新查了一下，正确的打开方式如下：

1. 到 http://ftp.gnu.org/gnu/wget/ 下载最新的wget源程序并解压
2. 然后运行./configure --with-ssl=openssl，那个openssl就是Mac上编译的核心选项，不然会默认使用GNUTLS，就编译不过去了。
	./configure --with-ssl=openssl
3. make
4. 编译好的wget在src目录下，要不要make install，还是自己拷贝就个人爱好了
4. wget --version 看看新编译的wget版本

	GNU Wget 1.16 built on darwin13.4.0.

	+digest +https +ipv6 -iri +large-file -nls +ntlm +opie -psl +ssl/openssl 

	Wgetrc: 
	    /usr/local/etc/wgetrc (system)
	Compile: 
	    gcc -DHAVE_CONFIG_H -DSYSTEM_WGETRC="/usr/local/etc/wgetrc" 
	    -DLOCALEDIR="/usr/local/share/locale" -I. -I../lib -I../lib -g -O2 
	Link: 
	    gcc -g -O2 -lssl -lcrypto -ldl -lz -liconv ftp-opie.o openssl.o 
	    http-ntlm.o ../lib/libgnu.a 

	Copyright (C) 2014 Free Software Foundation, Inc.
	License GPLv3+: GNU GPL version 3 or later
	<http://www.gnu.org/licenses/gpl.html>.
	This is free software: you are free to change and redistribute it.
	There is NO WARRANTY, to the extent permitted by law.

	Originally written by Hrvoje Niksic <hniksic@xemacs.org>.
	Please send bug reports and questions to <bug-wget@gnu.org>.

这样你就有了新的wget了。


