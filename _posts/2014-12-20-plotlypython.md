---
author: Longqi
comments: true
date: 2014-12-20 20:13:12
layout: post
slug: PlotlyPython
title: Matplotlib图像到Plot.ly
categories: [Plotly]
tags:
- Plotly
- Matplotlib
- Python
---
<iframe width="100%" height="480" frameborder="0" seamless="seamless" scrolling="no" src="https://plot.ly/~longqi/98.embed?width=640&height=480"></iframe>
[Plot.ly](https://plot.ly/) 可以将Matplotlib的图像转换成plot.ly的图片，用法在官网有[详细的讲解](https://plot.ly/matplotlib/)。不过，如果你想快速使用，那把这个文章看完也是个不错的选择哦！

安装Plot.ly的Python支持直接使用`pip`命令即可

{% highlight bash %}
pip install plotly
{% endhighlight %}


如果你第一次从Python中调用Plot.ly建议使用下面的操作：

{% highlight python %}
import plotly
plotly.tools.set_credentials_file(username='username', api_key='key')
{% endhighlight %}

这样以后就不用再次登录了。

之后的使用方法就和[ggplot里的情况]({% post_url 2014-12-20-plotlyr %})很相似了。这里改变了一下官网的例子，因为我平常不像官网那样使用Matplotlib。

{% highlight python %}
import plotly.plotly as py
import pylab as plt
n = 50
x, y, z, s, ew = np.random.rand(5, n)
c, ec = np.random.rand(2, n, 4)
area_scale, width_scale = 500, 5

sc = plt.scatter(x, y, c=c,
                s=np.square(s)*area_scale,
                edgecolor=ec,
                linewidth=ew*width_scale)
plt.grid()

plot_url = py.plot_mpl(plt.gcf())
{% endhighlight %}

这个代码的结果就是文章开头的图片了。是不是很简单啊？赶快将自己的图像也上传到plot.ly吧！

