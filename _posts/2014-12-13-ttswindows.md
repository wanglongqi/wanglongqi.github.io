---
author: Longqi
comments: true
date: 2014-12-13 11:17:50
layout: post
slug: TTSforWindows
title: Windows命令行下的TTS
published: True
categories: [System]
tags:
- Windows
- System
- Batch
- TTS
---

[Jampal mp3 Library](http://jampal.sourceforge.net/ptts.html)中提供了一个命令行下的TTS，除了选项和MAC OSX下的say命令不大一样，功能上还是非常相似的。直接使用如下格式就能调用：

{% highlight batch %}
cscript.exe ptts.vbs [options]
{% endhighlight %}

选项的解释如下：

<table border="1">
      <tr>
        <th width="100px">
          选项
        </th>
        <th>
          解释
        </th>
      </tr>
      <tr>
        <td>
          <code>-w filename</code>
        </td>
        <td>
          创建一个wave文件，而不是直接输出到音频。输出文件将是CD音质的，44100Hz的16位立体声文件。可以使用<code>-s</code>或<code>-c</code>修改。
        </td>
      </tr>
      <tr>
        <td>
          <code>-m filename</code>
        </td>
        <td>
          以空行为分隔符，生成多个wave文件。自动添加五位的数字到文件名。
        </td>
      </tr>
      <tr>
        <td>
          <code>-r rate</code>
        </td>
        <td>
          阅读速度 -10 到 +10. 默认是0.
        </td>
      </tr>
      <tr>
        <td>
          <code>-v volume</code>
        </td>
        <td>
          音量的百分比，默认是100.
        </td>
      </tr>
      <tr>
        <td>
          <code>-s samples</code>
        </td>
        <td>
          采样率，默认是44100.可选采样率为 8000, 16000, 22050, 44100, 48000.
        </td>
      </tr>
      <tr>
        <td>
          <code>-c channels</code>
        </td>
        <td>
          输出的声道数，默认为2。可设置为1或者2.
        </td>
      </tr>
      <tr>
        <td>
          <code>-u filename</code>
        </td>
        <td>
          从文件而不是标准输入读入文件。文件可以是Unicode，ANSi或者默认编码的。可使用<code>-e</code>选项指定。
        </td>
      </tr>
      <tr>
        <td>
          <code>-e encoding</code>
        </td>
        <td>
          指定输入文件的编码，可选项为ASCII,UTF-16LE. 默认为系统默认编码。
        </td>
      </tr>
      <tr>
        <td>
          <code>-voice xxxx</code>
        </td>
        <td>
          使用的TTS语音。
        </td>
      </tr>
      <tr>
        <td>
          <code>-vl</code>
        </td>
        <td>
          列出所有可用语音名称。
        </td>
      </tr>
    </table>

对于64位系统需要使用SysWow64中的`cscript`，命令的形式需要修改为：

{% highlight batch %}
C:\Windows\SysWOW64\cscript.exe ptts.vbs [options]
{% endhighlight %}

设置64bit系统的默认语音时，如果语音是32bit的，需要使用如下控制面板设置：

{% highlight batch %}
C:\Windows\sysWOW64\speech\SpeechUX\SAPI.cpl
{% endhighlight %}

当然，每次输入那么长的命令是很不科学的。可以建立一个叫`say.bat`的文件，内容为：

{% highlight batch %}
C:\Windows\SysWOW64\cscript.exe "%PATH_PTTS%\ptts.vbs" %*
{% endhighlight %}

这样就可以用形如`say [options]`的命令执行TTS任务了。

对于中文，如果系统的默认编码为GBK，可以使用如下命令输出中文语音（其中的字符编码按照实际文件改变）：

{% highlight batch %}
iconv -f UTF-8 -t GBK "%%i"|say -w %%~ni.wav
{% endhighlight %}

将目录下所有txt文件转换为语音文件大概可以用这样的批处理文件（个人偏好ogg，如果需要mp3可以用lame）：

{% highlight batch %}
for %%i in (*.txt) do (
	iconv -f UTF-8 -t GBK "%%i"|say -w %%~ni.wav && ffmpeg2theora.exe %%~ni.wav
	)
{% endhighlight %}

想看懂有不大看得懂`%~ni`的同学可以参见[批处理中for循环怎么去掉变量的后缀名]({% post_url 2014-11-18-variableinforloop %})。

对了，最后共享一个[`ptts.vbs`](/public/other/ptts.vbs)，以防原项目不能访问了。


2014-12-14 更新：

对于中文，如果系统的默认编码为GBK，可以使用如下命令输出中文语音（其中的字符编码按照实际文件改变）：

{% highlight batch %}
iconv -f UTF-8 -t GBK "%%i"|say -w %%~ni.wav
{% endhighlight %}

但是，如果文件中有非GBK字符，`iconv`会自动退出。所以可以稍微修改命令行使`iconv`忽略GBK的非法字符。命令如下：

{% highlight batch %}
iconv -c -f UTF-8 -t GBK "%%i"|say -w %%~ni.wav
{% endhighlight %}

`iconv`还是比较有用的命令，等有时间单独介绍一下。

