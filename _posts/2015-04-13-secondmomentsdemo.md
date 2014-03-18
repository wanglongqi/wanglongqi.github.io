---
author: Longqi
comments: true
date: 2015-04-13 15:00:11
layout: post
slug: secondmomentsdemo
title: 真的有必要考试考求惯性矩吗？
categories: [Opinion]
tags:
- Sympy
- Python
---
![Python](/public/images/python.png)
## 引言
我一直认为没有必要在考试中求截面矩和质心一类玩意（某校有一门课好像主要就在考求L形啊，I形的截面矩，我就不点名了）。因为现在的电脑（其实手机也可以）太容易求出这些几何性质的量了，而且实际上，这个求惯性矩的代码只有几行长，可以参见今天下午的另外一个文章里的代码。况且，ANSYS和AutoCAD都内置了相关函数。有人可能会说，那几个软件里只能求数值解，我要说其实就算要求解析解也不困难，这里就做个演示。


    from sympy import Polygon, Point, var, init_printing, simplify
    import sympy
    init_printing()
    var('b,h,t')
    from second_moments import second_moments
   

## 矩形截面：
假设宽为b，高为h。

    p = map(Point,((0,0),(b,0),(b,h),(0,h)))
    poly = Polygon(*p)
    poly.area


$$b h$$

    poly.centroid

$$Point(b/2, h/2)$$




    Ix, Iy, Ixy = second_moments(poly)
    Ix, Iy, Ixy




$$\left ( \frac{b h^{3}}{12}, \quad \frac{b^{3} h}{12}, \quad 0\right )$$



## L形截面
假设厚度都是t,宽为b，高为h


    p = map(Point,((0,0),(b,0),(b,t),(t,t),(t,h),(0,h)))
    poly = Polygon(*p)
    poly.area




$$t \left(b + h - t\right)$$




    simplify(poly.centroid)




$$Point((b**2 + h*t - t**2)/(2*(b + h - t)), (b*t + h**2 - t**2)/(2*(b + h - t)))$$




    Ix, Iy, Ixy = simplify(second_moments(poly))
    Ix, Iy, Ixy




$$\left ( \frac{t}{12 b + 12 h - 12 t} \left(b^{2} t^{2} + 4 b h^{3} - 6 b h^{2} t + 4 b h t^{2} - 2 b t^{3} + h^{4} - 4 h^{3} t + 6 h^{2} t^{2} - 4 h t^{3} + t^{4}\right), \quad \frac{t}{12 b + 12 h - 12 t} \left(b^{4} + 4 b^{3} h - 4 b^{3} t - 6 b^{2} h t + 6 b^{2} t^{2} + 4 b h t^{2} - 4 b t^{3} + h^{2} t^{2} - 2 h t^{3} + t^{4}\right), \quad \frac{b h t \left(b h - b t - h t + t^{2}\right)}{- 4 b - 4 h + 4 t}\right )$$



你实际上还可以得到$t$是小量时候的二阶近似


    simplify(sympy.series(Ix,t,n=2).removeO())




$$\frac{h^{3} t \left(4 b + h\right)}{12 b + 12 h}$$




    simplify(sympy.series(Iy,t,n=2).removeO())




$$\frac{b^{3} t \left(b + 4 h\right)}{12 b + 12 h}$$




    simplify(sympy.series(Ixy,t,n=2).removeO())




$$- \frac{b^{2} h^{2} t}{4 b + 4 h}$$



## 六边形：
外接圆半径为R的吧！


    var('R')
    p = [(sympy.cos(i)*R,sympy.sin(i)*R) for i in arange(6)/sympy.S.One/3*sympy.pi]
    poly = Polygon(*p)
    p




$$\left [ \left ( R, \quad 0\right ), \quad \left ( \frac{R}{2}, \quad \frac{\sqrt{3} R}{2}\right ), \quad \left ( - \frac{R}{2}, \quad \frac{\sqrt{3} R}{2}\right ), \quad \left ( - R, \quad 0\right ), \quad \left ( - \frac{R}{2}, \quad - \frac{\sqrt{3} R}{2}\right ), \quad \left ( \frac{R}{2}, \quad - \frac{\sqrt{3} R}{2}\right )\right ]$$




    poly.area




$$\frac{3 \sqrt{3}}{2} R^{2}$$




    poly.centroid




$$Point(0, 0)$$




    second_moments(poly)




$$\left ( \frac{5 \sqrt{3}}{16} R^{4}, \quad \frac{5 \sqrt{3}}{16} R^{4}, \quad 0\right )$$




    
