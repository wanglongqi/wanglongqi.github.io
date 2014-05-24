---
author: Longqi
comments: true
date: 2014-03-24 06:24:59+00:00
layout: post
slug: '%e6%a0%b9%e6%8d%ae%e7%a6%bb%e6%95%a3%e7%82%b9%e5%87%bd%e6%95%b0%e5%80%bc%e7%bb%98%e5%88%b6%e7%ad%89%e9%ab%98%e7%ba%bf%e7%9a%84%e6%96%b9%e6%b3%95'
title: 根据离散点函数值绘制等高线的方法
wordpress_id: 250
tags:
- Python
- 等高线
- 绘图方法
---

前两天有人找我帮忙解决一个振动区域分级的问题，问题的细节描述比较复杂，牵涉到一些振动评价方法的问题。不过划归到最后可以将问题等效为给定离散点的函数值，获得区域等高线的方法。这个问题其实不复杂，特别是对于绘制过噪声地图的人。但是由于大多数人仅接触过基于Grid数据绘图的方法，对于这一问题往往无从下手。下面我们就来介绍一下解决这个问题的最为常用的方法。




由离散点的函数值插值获得曲面实际上是一个非常常见的过程。在有限元计算中，这是后处理的关键一步，也即将高斯点的位移值推广到单元节点上。其中最简单的方法是线性插值，根据单元的不同可以使用相应的插值函数将高斯积分点上的函数值推广到全场上。然后由于各单元的应变值对于C0单元是不连续的，有限元中会提出很多相关的应力磨平方法。这些问题在使用离散点函数值绘制曲面或等高线是都会遇到。但是根据问题的不同，使用的插值方法也应有相应的改变。比较常见的几种选择是线性插值、最近邻插值和自然样条插值。


<!-- more -->


## 线性插值方法




线性插值是解决将离散点函数值插值到曲面上最为简单的方法，其基本思想和线性三角单元的插值方式是完全一致的。唯一的区别在于离散点需要首先形成三角形网格。这一问题可以使用[Qhull](http://qhull.org/)提供的函数快速的完成。下面引用一段[Scipy](http://www.scipy.org/)中实现ND线性插值的代码，该代码使用了[Cython](http://cython.org)技术，用于加速插值的过程。不过其计算流程是清晰的。首先是39行，程序使用[Qhull](http://qhull.org/)对给定点进行了三角化，这样就形成了有限元计算中的网格；然后第78行qhull._find_simplex可以给出需要输出点所在的网格；最后95～96行完成了线性插值的工作。整个流程和线性三角形网格的位移推广方法是一致的。



{% highlight python %}
    
    #------------------------------------------------------------------------------
    # Linear interpolation in N-D
    #------------------------------------------------------------------------------
    
    class LinearNDInterpolator(NDInterpolatorBase):
        """
        LinearNDInterpolator(points, values, fill_value=np.nan)
    
        Piecewise linear interpolant in N dimensions.
    
        .. versionadded:: 0.9
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndims); or Delaunay
            Data point coordinates, or a precomputed Delaunay triangulation.
        values : ndarray of float or complex, shape (npoints, ...)
            Data values.
        fill_value : float, optional
            Value used to fill in for requested points outside of the
            convex hull of the input points.  If not provided, then
            the default is ``nan``.
    
        Notes
        -----
        The interpolant is constructed by triangulating the input data
        with Qhull [1]_, and on each triangle performing linear
        barycentric interpolation.
    
        References
        ----------
        .. [1] http://www.qhull.org/
    
        """
    
        def __init__(self, points, values, fill_value=np.nan):
            NDInterpolatorBase.__init__(self, points, values, fill_value=fill_value)
            if self.tri is None:
                self.tri = qhull.Delaunay(self.points)
    
        def _evaluate_double(self, xi):
            return self._do_evaluate(xi, 1.0)
    
        def _evaluate_complex(self, xi):
            return self._do_evaluate(xi, 1.0j)
    
        @cython.boundscheck(False)
        @cython.wraparound(False)
        def _do_evaluate(self, double[:,::1] xi, double_or_complex dummy):
            cdef double_or_complex[:,::1] values = self.values
            cdef double_or_complex[:,::1] out
            cdef double[:,::1] points = self.points
            cdef int[:,::1] simplices = self.tri.simplices
            cdef double c[NPY_MAXDIMS]
            cdef double_or_complex fill_value
            cdef int i, j, k, m, ndim, isimplex, inside, start, nvalues
            cdef qhull.DelaunayInfo_t info
            cdef double eps, eps_broad
    
            ndim = xi.shape[1]
            start = 0
            fill_value = self.fill_value
    
            qhull._get_delaunay_info(&info, self.tri, 1, 0)
    
            out = np.zeros((xi.shape[0], self.values.shape[1]),
                           dtype=self.values.dtype)
            nvalues = out.shape[1]
    
            eps = np.finfo(np.double).eps * 100
            eps_broad = sqrt(np.finfo(np.double).eps)
    
            with nogil:
                for i in xrange(xi.shape[0]):
    
                    # 1) Find the simplex
    
                    isimplex = qhull._find_simplex(&info, c,
                                                   &xi[0,0] + i*ndim,
                                                   &start, eps, eps_broad)
    
                    # 2) Linear barycentric interpolation
    
                    if isimplex == -1:
                        # don't extrapolate
                        for k in xrange(nvalues):
                            out[i,k] = fill_value
                        continue
    
                    for k in xrange(nvalues):
                        out[i,k] = 0
    
                    for j in xrange(ndim+1):
                        for k in xrange(nvalues):
                            m = simplices[isimplex,j]
                            out[i,k] = out[i,k] + c[j] * values[m,k]
    
            return out

{% endhighlight %}


## 最近邻插值方法




最近邻插值是将空间按照输入点划分为不同区域，然后认为需求点的函数值和与其最近点的函数值一致。这个方法的实现可以使用[_k-_d树](https://en.wikipedia.org/wiki/K-d_tree)完成，下面是[Scipy](http://www.scipy.org/)中最近邻ND插值的实现代码。 算法的流程很贱但，首先将坐标点形成[_k-_d树](https://en.wikipedia.org/wiki/K-d_tree)（第25行），然后对树进行查询（第41行）就可以确定应该使用那个现有值返回作为需要输出点的函数值，最后输出对应的函数值就完成了最近邻插值了。



{% highlight python %}
    
    class NearestNDInterpolator(NDInterpolatorBase):
        """
        NearestNDInterpolator(points, values)
    
        Nearest-neighbour interpolation in N dimensions.
    
        .. versionadded:: 0.9
    
        Parameters
        ----------
        points : (Npoints, Ndims) ndarray of floats
            Data point coordinates.
        values : (Npoints,) ndarray of float or complex
            Data values.
    
        Notes
        -----
        Uses ``scipy.spatial.cKDTree``
    
        """
    
        def __init__(self, x, y):
            x = _ndim_coords_from_arrays(x)
            self._check_init_shape(x, y)
            self.tree = cKDTree(x)
            self.points = x
            self.values = y
    
        def __call__(self, *args):
            """
            Evaluate interpolator at given points.
    
            Parameters
            ----------
            xi : ndarray of float, shape (..., ndim)
                Points where to interpolate data at.
    
            """
            xi = _ndim_coords_from_arrays(args)
            xi = self._check_call_shape(xi)
            dist, i = self.tree.query(xi)
            return self.values[i]

{% endhighlight %}


## 样条插值方法




与其他两种方法相比，样条插值方法要复杂得多。在这里就不做具体的介绍了，有兴趣的话可以参考以下文献：





> 

> 
> 1. P. Alfeld, A trivariate Clough-Tocher scheme for tetrahedral data. Computer Aided Geometric Design, 1, 169 (1984);
> 
> 

> 
> 2. G. Farin, Triangular Bernstein-Bezier patches .Computer Aided Geometric Design, 3, 83 (1986).
> 
> 





这一方法的具体实现可以参见[Scipy](http://www.scipy.org/)中CloughTocher2DInterpolator和double_or_complex _clough_tocher_2d_single函数的实现。





## 范例




下面沿用[Scipy](http://www.scipy.org/)文档中给出一个使用上述三种方法进行插值和等高线绘制的例子，帮助大家理解这些方法的区别和特点。




首先，我们先生成一些测试用的数据：




{% highlight python %}    
    def gen(x,y):
       return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2
    points = np.random.rand(1000, 2)
    values = gen(points[:,0], points[:,1])
    xi = np.mgrid[0:1:100j, 0:1:200j]
    xi=reshape(xi,(2,-1)).T
{% endhighlight %}



然后，我们分别使用三种不同的方法对上述离散点进行插值：



{% highlight python %}
    
    z0 = griddata(points, values, xi, method='nearest')
    z1 = griddata(points, values, xi, method='linear')
    z2 = griddata(points, values, xi, method='cubic')

{% endhighlight %}


最后，对这些值绘制等高线：




{% highlight python %}    

    xi = np.mgrid[0:1:100j, 0:1:200j]   
    contourf(xi[0],xi[1],reshape(z0,(100,-1)))
    contourf(xi[0],xi[1],reshape(z0,(100,-1)))
    contourf(xi[0],xi[1],reshape(z0,(100,-1)))
    
{% endhighlight %}

[![figure_1](http://bcs.duapp.com/pecker/figure_1_thumb.png)](http://bcs.duapp.com/pecker/figure_1.png)




[![figure_2](http://bcs.duapp.com/pecker/figure_2_thumb.png)](http://bcs.duapp.com/pecker/figure_2.png)




[![figure_3](http://bcs.duapp.com/pecker/figure_3_thumb.png)](http://bcs.duapp.com/pecker/figure_3.png)




可以看到，根据实际需求的不同应该选用不同的方法解决问题，线性插值可以获得多边形的区域划分，最近邻获得的是一个个色块（等效于Voronoi图），而样条插值可以获得比较光滑的等高线。具体使用什么样的插值方式往往是问题相关的，对于特殊的问题也可以使用类似的想法开发对应的插值算法。这时，有限元的后处理方法往往可以提供一些有用的参考。
