---
author: Longqi
comments: true
date: 2014-03-24 13:29:28+00:00
layout: post
slug: implement-of-lagrange-polynomial-in-sympy
title: Implement of Lagrange Polynomial in Sympy
categories: [Python]
tags:
- Python
- Sympy
---
![Python Related Posts](/public/images/python.svg)
Lagrange Polynomial has a general form like:

$$L_i(x)=\prod_{j=1,j\neq i}^{n} \frac{x-x_j}{x_i-x_j}$$

Its parameters include:

	
  1. $n$: number of given points,

	
  2. $x_i$: coordinates of interpolation points,

	
  3. order: n-1, the max power in the poly.,

	
  4. $L_i$: Lagrange Poly. at point $i$ ($i$ start from 0).


We introduce a Sympy implement for the polynomial, since we do not find an official implement. The code is presented here:

    
    def LagrangPoly(x,order,i,xi=None):
        if xi==None:
            xi=symbols('x:%d'%(order+1))
        index = range(order+1)
        index.pop(i)
        return prod([(x-xi[j])/(xi[i]-xi[j]) for j in index])



This function is rather easy. But yeah it can generate any one variable Lagrange Polynomial. Here is some examples:


    
    x=symbols('x')
    LagrangPoly(x,5,0)



$$\frac{\left(x - x_{1}\right) \left(x - x_{2}\right) \left(x - x_{3}\right) \left(x - x_{4}\right) \left(x - x_{5}\right)}{\left(x_{0} - x_{1}\right) \left(x_{0} - x_{2}\right) \left(x_{0} -x_{3}\right) \left(x_{0} - x_{4}\right) \left(x_{0} - x_{5}\right)}$$

Since the parameter xi only needs to be a sequence, the function works with any Sympy supported sequence whether a list or a numpy array. Here we pass a Python list into the function.
    
    x=symbols('x')
    simplify(LagrangPoly(x,2,0,[-1,0,1])),
    simplify(LagrangPoly(x,2,1,[-1,0,1])),
    simplify(LagrangPoly(x,2,2,[-1,0,1]))


\begin{pmatrix}\frac{1}{2} x \left(x -1\right), & - x^{2} + 1, & \frac{1}{2} x \left(x + 1\right)\end{pmatrix}

And the sum of upper three polynomials is 1, of course. It is simple to implement Hermite polynomial by Langange polynomial, which will be left for you practice.

