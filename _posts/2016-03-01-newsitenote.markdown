---
author: YiZi
comments: true
date: 2016-03-01 14:29:21 +0800
layout: post
slug: NewSiteNotes
title: 新版网站制作手记
categories: [Website]
tags:
- 网站相关
---
![WhyHow](//whyhow.github.io/public/index.svg)
自从前几天宣布网站将迎来另一位作者之后，我极速的推进了计划已久的新版网站计划。一方面，老的网站的域名太长，不适合作为主要交流平台；另一方面，新的网站使用了更为个性化的架构。因此，我在这里记录一下新网站的设计的基本想法。

老的网站基本是基于Hyde模板在Jekyll上架构的，整体设计思路是Jekyll官方的设计方案。说实话，我很不喜欢，最不喜欢的一点是如果基于Github的平台发布，你不能为Jekyll添加或者编写新的插件，而只能在现有的功能很弱的Jekyll的基础上实现各种功能。显然地，很多功能是无法在这个架构下完成的（我想我不用列举了，使用Jekyll在Github建站的读者都肯定遇到过各种各样的问题）。因此，新版网站的革命性的改变是“完全的定制化”，而实现这一点我不得不做出的牺牲是“仅支持支持Javascript语言的浏览器”。很多人肯定要跳出来，你这个不符合Responsive Design的理念、效率不够高等等等等问题。我只能说，这些都是问题，但是对于我们自己做得一个小网站而且还要使用Github的平台，这些问题都不是问题，等到这些真正成为问题的时候，我会着手解决他们的。下面就是我做得几个完全不符合各种线代设计理念的设计方案：

## 直接扔掉所有文章的列表页面
Jekyll默认会将所有文章列表到一个页面，然后那个页面可以分页，可以显示缩略文本，功能很好。然而这个想法和新网站的想法直接冲突，所以这也是最早被扔到垃圾堆的功能。新的网站直接打开将是网站的模块，而不是文章的列表，实际上，我们并不希望在某个页面显示Jekyll的默认文章列表（其实也是有的，不过那是这个网站的机读页面，也即RSS Feed）。文首就是我们新的网站的主页分块方案。

## 固定网站的版块
按照基本的设计思想，网站的设计应该容易扩展。但是我们通过商量决定，我们将使用固定的网站版块设计并将版块设计的思路直接硬编码到网站的源码中。这可能是我们短视，不过这一固定的网站版块设计使得我可以穷举所有的版块，由此可以克服各种各样Jekyll带来的困难。我相信，至少短期来看这个选择是正确的，而且对于新的网站也是必要的。（如果用自己的机器，那么这将是完全另外一个Story）

## 完全基于Javascript的页面载入机制
默认的Jekyll不支持按照类别分页显示文章，这一点是使用固定的网站版块设计之后面临的第一个困难。为此，我抛弃了整个Responsive Design的理念，直接假设所有用户都启用了Javascript。这自然是相当鲁莽了，先不说那些用不支持Javascript浏览器的用户（其实不会太多），对于那些我“特别尊敬”的还在使用诸如NoScript的用户只能表示异常抱歉。因为，无分页功能的分类文章列表是完全无法忍受的（即便是只显示文章概要）。因此，我们使用了基于无限滚动加载的页面模式，每次都会读入文章的全文，但是文章不会载入，除非用户滚到页面底端。这个逻辑的设计在网站的Javascript脚本里进行了编写：

{% highlight javascript %}
var fetchingContent = false;

function yHandler() {
    var wrap = $('.posts')[0];
    var contentHeight = wrap.offsetHeight;
    var yOffset = window.pageYOffset;
    var y = yOffset + window.innerHeight;

    if (y >= contentHeight && !fetchingContent) {
        fetchingContent = true;
        $(".load:last").load(urls[index] + " div.post",function(){
        index += 1;
        if (index >= urls.length) {
            fetchingContent = true;
            $('#next').removeAttr('href');
            $('#next').html('未发现更多内容');
        } else {
            fetchingContent = false;
            $('.posts').append('<div class="load"/>');
            $('#next').attr('href', urls[index]);
        }
        yHandler();  
    });
    }
}
{% endhighlight %}

## 分类的文章查看方法
基于无限滚动的文章载入方式对于查看网站最新文章的用户来说无疑是最佳的设计方案之一，但是对于需要看历史文章的用户将带来极大的困难。所以网站需要提供一个对于需要查看历史文章的途径。在这里我们并没有想出太好的解决方案，不过固定版块的设计思路帮助了我们实现了现在网站上看到的，每个分类可以在页首的时候查看到这个分类的索引的目的。当然，将索引硬编码到这个页面中也不是不行，这方面我并没有做太细致的思考，可能这才是正确的打开方式。

## 新网站的网址
其实文首的图片已经泄露了新网站的地址，新的网址是：[https://whyhow.github.io](//whyhow.github.io)，欢迎大家来新的网站访问，虽然现在网站还在建设当中。
