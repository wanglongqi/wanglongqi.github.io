---
layout: post
title: "post.excerpt Not Working as Expected"
date: 2014-03-24T15:41:09+08:00
---

Jekyll is a very silly converter for website, but Github uses it. I changed post.content to post.excerpt in the template page, but nothing happens. Firstly, I thought Jekyll used by Github do not support this variable. However, I found some of the posts only display excerpt, but others display whole content. What is happening? After a full investigation, I find out the difference between two kinds of pages are the wrapping character. In some files CR+LF are used, as a default option for Windows platform, in other files LF are used, as the default option of \*nix platform. Jekyll is working well with LF, but not with CR+LF. The solution for this problem is to convert all CR+LF to LF. An easy way to do this is use dos2unix command. 
