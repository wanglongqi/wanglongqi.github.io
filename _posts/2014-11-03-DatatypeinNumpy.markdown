---
author: Longqi
comments: true
date: 2014-11-03 23:46:58
layout: post
slug: DataTypeinNumpy
title: Numpy里的Float是单精度还是双精度？
categories: [Python]
tags:
- Python
- Tutorial
---
![Python Related Posts](/public/images/python.png)
Float在C里面是单精度的，那么在Numpy里面也是单精度的吗？

答案是双精度的，因为这是Numpy的数据类型列表：

	Data type	Description
	bool	Boolean (True or False) stored as a byte 布尔类型，一个字节
	int	Platform integer (normally either int32 or int64) 整型，几位系统几位整型
	int8	Byte (-128 to 127) 8位整型
	int16	Integer (-32768 to 32767) 16位整型
	int32	Integer (-2147483648 to 2147483647) 32位整型
	int64	Integer (9223372036854775808 to 9223372036854775807) 64位整型
	uint8	Unsigned integer (0 to 255) 无符号8位整型
	uint16	Unsigned integer (0 to 65535) 无符号16位整型
	uint32	Unsigned integer (0 to 4294967295) 无符号32位整型
	uint64	Unsigned integer (0 to 18446744073709551615) 无符号64位整型
	float	Shorthand for float64. *双精度浮点型*
	float16	Half precision float: sign bit, 5 bits exponent, 10 bits mantissa 16位浮点型
	float32	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa 单精度浮点型
	float64	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa 双精度浮点型
	complex	Shorthand for complex128. 双精度复数
	complex64	Complex number, represented by two 32-bit floats (real and imaginary components) 单精度复数
	complex128	Complex number, represented by two 64-bit floats (real and imaginary components) 双精度复数

对了，scipy里有float128哦，四精度的浮点型，给力啊！