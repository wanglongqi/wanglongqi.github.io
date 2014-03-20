---
layout: post
title: "Hello World!"
tags: "Test","Tag Test"
date: 2014-03-19T18:10:55+08:00
---

Since GitHub SVN interface does not allow empty directory, This is a test post! Latex Equation and Code Highlight are tested in this post. Meanwhile tags function is also tested in this post.

## [MathJax](http://www.mathjax.org/) Test

Pass with kramdown, fail in redcarpet.

* Basic equation

    $$kx+m\ddot{x} = p_0 \sin \omega t$$

* Solution

    $$x=C_1  \cos(\omega_nt + \phi) +  \frac{p_0}{k (1-\beta^2)}\sin \omega t$$
    
where, $\beta=\omega/\omega_n$

* Remarks
    * in undamped case, the phase of response is either 0, or $\pi$. 
    * $R_d=1/\mathrm{abs}(1-\beta^2)$
    
## Highlight Test
Not compatible with MathJax, color is awful. Disabled.

{% highlight python %}
def effect(self):
    self.options.scale=float(self.options.scale)
    action=self.options.action.strip("\"")
    if action=="viewold":
        for i in self.options.ids:
            node=self.selected[i]
{% endhighlight %}

End of test file.
