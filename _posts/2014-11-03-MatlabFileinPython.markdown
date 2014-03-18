---
author: Longqi
comments: true
date: 2014-11-03 22:56:58
layout: post
slug: MatlabFileinPython
title: Python中处理Matlab文件
categories: [Python]
tags:
- Python
- Tutorial
- Matlab
---
![Python Related Posts](/public/images/python.png)
作为一个老的Matlab用户，自然会有很多Matlab格式的数据文件，迁移到Python之后第一步就是怎么读取Matlab数据文件。Matlab的数据文件分为两种，后缀都是.mat，旧的Matlab文件是私有格式；新的Matlab文件是HDF5的封装。

## 旧版Matlab文件的读写

旧版Matlab文件是指兼容v7.2及以前版本.mat格式文件，读写这种文件可以使用Scipy中的函数。读取的代码如下：

{% highlight python %}
from scipy.io import loadmat
data=loadmat(filename)
{% endhighlight %}

几个可能有用的选项有：

	appendmat : 设置为True，如果给定文件名没有.mat后缀，会自动往文件名后添加.mat	
	mat_dtype : 设置为True，将数组按Matlab的格式约定载入文件
	squeeze_me : 设置为True，会自动剪除空白维度
	matlab_compatible : 设置为True，将按Matlab的格式约定载入文件
	struct_as_record : 设置为True，将Matlab文件中的结构体载入为record数组

写入旧版Matlab文件可使用savemat函数完成。代码如下：

{% highlight python %}
from scipy.io import savemat
data={}
data['var1']=arange(10)
savemat(filename,data,do_compression=True)
{% endhighlight %}

几个可能有用的选项有：

	appendmat :  默认为True，如果给定文件名没有.mat后缀，会自动往文件名后添加.mat	
	do_compression : 默认为False。设置为True，压缩mat文件
	oned_as : 一维数组存储为行向量还是列向量。低版本Scipy默认是列，高版本Scipy默认是行。如果要固定的话，最好给定这个参数。

## 新版Matlab文件的读写

新版Matlab文件就是HDF5的封装，所以直接用HDF5的Python库就能读取。根据不同人的喜好有多种不同选项，有需要的可以Google。但是.mat不等同与HDF5文件，用现成的HDF5库存储的文件Matlab中不能作为.mat文件打开。

对了，scipy.io里还有一个whosmat文件可以用来查看mat文件中的变量。

