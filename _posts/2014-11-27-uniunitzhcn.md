---
author: Longqi
comments: true
date: 2014-11-27 11:59:00
layout: post
slug: uniUnitReadMe
title: uniUnit - 统一单位系统的程序包
published: True
categories: [uniunit]
tags:
- uniUnit
---
![uniUnit](/public/images/uniUnit128.png)
有限元和类似计算方法往往是无量纲的，而实际的计算是需要一个量纲的，因此计算人员必须保证模型中量的量纲是一致的。这是一个很繁杂的工作，大部分计算人员都或多或少的在这个问题上犯过错误。因此，在这里我写了一个程序包来彻底的解决这个问题。

这个程序包的想法很简单。首先，你需要告诉我你想要的量纲系统。其次，你需要告诉我一个正确的量。然后一切就搞定了，程序包会返回在你指定的量纲系统中量的值是多少。

这里是几个例子：

{% highlight python %}
from uniunit import *
conv_dict = {'kg':'g','m':'mm','s':'s',
			'A':'mA','K':'K','mol':'mol','cd':'cd'}
myunit = uniUnit(conv_dict)

myunit.to_unit(100 * kg)
# 100000.0 [g]
{% endhighlight %}

哈，这样的功能有谁会需要，太简单了！好吧，那下面这个例子怎么样呢？

{% highlight python %}
myunit.to_unit(J)
# 1000000000.0 [g.mm2/s2]

myunit.to_unit(W/m/m)
# 1000.0 [g/mm0.s3]

W/m/m == kg/s/s/s
# True
{% endhighlight %}

或者，如果你是个纳米科学专家，你可能喜欢用纳米为单位的量。

{% highlight python %}
conv_dict = {'kg':'ug','m':'nm','s':'ps',
			'A':'mA','K':'K','mol':'mol','cd':'cd'}
myunit1 = uniUnit(conv_dict)

myunit1.to_unit(2E11*Pa)
# 2e-13 [ug/nm.ps2]
{% endhighlight %}

还是很简单吗？那如果不是国际单位制呢？试试告诉我`1 W/m/m`在`pound, inch, min`的量纲系统中是多少？

{% highlight python %}
conv_dict = {'kg':'pound','m':'inch','s':'min'}
myunit2 = uniUnit(conv_dict)

myunit2.to_unit(W/m/m)
# 476198.486319 [pound/inch0.min3]

1*W/m/m - 476198.486319*pound/min**3
#  7.04547531427e-13 [W/m2]
{% endhighlight %}

备注: 

- 你不需要提供整个量纲对应表，只需要提供你需要用到的那些；
- 但是，你必须提供你需要用到的所有量纲的对应表，因为对应表是没有默认值的；
- 你还可以用自定义的量纲系统。这里是一个例子：

{% highlight python %}
Long = unum.Unum.unit('Long',1000*km)
Flash = unum.Unum.unit('Flash',1*ms)

conv_dict = {'m':'Long','s':'Flash'}

myunit3 = uniUnit(conv_dict)

myunit3.to_unit(m)
# 1e-06 [Long]

myunit3.to_unit(9.8 * m/s**2)
# 9.8e-12 [Long/Flash2]

{% endhighlight %}


在你开始之前，下面这些内容可能你会感兴趣：

- `1 [T]` 不是 `1000 [kg]`, 而是 `1 特斯拉`；
- `in` 是Python的保留字，不能用来作为单位。


库的依赖关系
============
[unum](https://pypi.python.org/pypi/Unum) - 你可以用 `easy_install unum`安装它


开发计划？
==========
这里列出了几个可能的扩展:

- 图形界面: 个人偏好Qt的界面.
- Numpy和list的支持: 可能有用，不很确定.
- 单位化简: 可能有意思，有一些想法，不过还不很清晰。
- 添加更多的预定义单位: 应该是有用的，应该会在后续添加。
- 添加测试模块: 开发过程已经用了一个简单的测试脚本，可能nose的测试系统不大好。不过， 测试模块肯定是需要的。
- 文档: 应该不用了，这么简单的模块还用文档吗？我觉得这个介绍和[网站上的文章](https://wanglongqi.github.io/uniUnit/)应该够了。
