---
author: Longqi
comments: true
date: 2014-12-22 13:36:16
layout: post
slug: PlotlyMatlab
title: Matlab图像到Plot.ly
categories: [Plotly]
tags:
- Plotly
- Matlab
---
<iframe width="100%" height="486" frameborder="0" seamless="seamless" scrolling="no" src="https://plot.ly/~MATLABAPI/94.embed?width=640&height=486"></iframe>
[Plot.ly](https://plot.ly/) 可以将Matlab的图像转换成plot.ly的图片。由于我最近不用Matlab，所以就简单的介绍一下Plot.ly在Matlab下的安装和使用。

先到以下网址下载Plot.ly的工具箱[https://github.com/plotly/MATLAB-api/archive/master.zip](https://github.com/plotly/MATLAB-api/archive/master.zip).

然后，运行一下命令：

{% highlight matlab %}
cd MATLAB-api-master
plotlysetup('username', 'key')
{% endhighlight %}

这样就可以了。使用方法很简单：

{% highlight matlab %}
[X,Y,Z] = peaks;
contour(X,Y,Z,20);

fig2plotly()
{% endhighlight %}

返回值里会有生成的图像的URL。对了更新工具箱可以用以下命令：

{% highlight matlab %}
plotlyupdate
{% endhighlight %}
