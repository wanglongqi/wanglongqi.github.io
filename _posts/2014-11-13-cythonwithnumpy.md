---
author: Longqi
comments: true
date: 2014-11-13 12:52:27
layout: post
slug: CythonwithNumpy
title: 使用了Numpy的Cython程序编译错误解决方案
categories: [Python]
tags:
- Python
- Cython
- Numpy
- Compile
---
![Python](/public/images/python.png)
这是个老问题了，典型的错误提示信息是 `fatal error: numpy/arrayobject.h: No such file or directory...compilation terminated error` 。 为了避免每次都去翻笔记共享到这里，也方便遇到同样问题的同学解决。[原帖在这里](https://stackoverflow.com/questions/14657375/cython-fatal-error-numpy-arrayobject-h-no-such-file-or-directory)

解决方案中Robert Kern提到：

{% highlight python %}
In your `setup.py`, the Extension should have the argument `include_dirs=[numpy.get_include()]`.

Also, you are missing `np.import_array()` in your code.

--

Example setup.py:

from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=[
        Extension("my_module", ["my_module.c"],
                  include_dirs=[numpy.get_include()]),
    ],
)

# Or, if you use cythonize() to make the ext_modules list,
# include_dirs can be passed to setup()

setup(
    ext_modules=cythonize("my_module.pyx"),
    include_dirs=[numpy.get_include()]
)  
{% endhighlight %}

  

解决方法就是往`include_dirs`添加`numpy.get_include()`。

