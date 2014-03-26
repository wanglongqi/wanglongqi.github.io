---
layout: post
title: "HWG702: Howto Find the Average"
date: 2014-03-26T11:21:18+08:00
---

Hello, everyone from HWG702. This page provides supplementary materials for microteaching session. In the microteaching session, the lecture is self-contained, no background is assumed. In this page, basic understanding of statistics and probability is assumed.
In the lecture, we will discuss the various indexes on measuring average in our daily life ([mid-range]( http://en.wikipedia.org/wiki/Mid-range) is not covered in the session, due to time concern). 

In this page, we present results on some well-known distributions to demonstrate the some of the ideas discussed in the session. Here are expected mean, mode and median value of samples from Exponential, LogNormal and Normal distributions, repectively.

## Normal distribution
![norm](https://wanglongqi.github.io/public/images/norm.png)

As is shown in the above figure, samples from Normal distribution have the same mean, mode and median. In addition, [central limit theorem]( http://en.wikipedia.org/wiki/Central_limit_theorem) says that “the arithmetic mean of a sufficiently large number of iterates of independent random variables, each with a well-defined expected value and well-defined variance, will be approximately normally distributed”. Therefore, in many cases, mean, mode and median are approximately the same in our daily life. This this the hidden reason why we do not distinguish between the indexes. However, there are cases do matters, if you use wrong index.

## Exponential distribution
![expo](https://wanglongqi.github.io/public/images/expon.png)

Samples from exponential distribution are clearly skewed. Most of the samples are located near zero. In this case, mode is obviously not a suitable index for this distribution. The other two indexes return similar results. In fact, expected mean value and median have following relation:

$$\mathrm{Median}=\ln 2 \mathrm{Mean} =\frac{\ln 2}{\lambda}$$

where, $\lambda$ is the only parameter of exponential distribution.

## LogNormal distribution
![lognorm](https://wanglongqi.github.io/public/images/lognorm.png)

Samples from lognormal have median located between mode and mean value, which is also a common phenomenon in our daily life. The tail of some common distributions (negligible amount of outliers are presented), like lognormal distribution, makes the median larger than mean value. As is discussed in the session, the presents of outliers is the reason why annual income of Beijing is much higher than it should be.

## Additional notes
Some distributions have well-defined median and mode, but have undefined mean value, such as Cauchy distribution. The derivation of the conclusion requires a bit mathematics, you can refer to [this page]( http://en.wikipedia.org/wiki/Cauchy_distribution#Mean) for more details.

