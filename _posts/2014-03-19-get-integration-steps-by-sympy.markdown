---
layout: post
title: "Get Integration Steps by Sympy"
date: 2014-03-19T22:44:57+08:00
---

This post trys to convert a IPython notebook to markdown document by nbconvert.

    from intsteps import *
    from sympy import *
    from IPython.display import HTML
    init_printing()


    x=symbols('x',real=1)

## Simple integral by part


    HTML(print_html_steps(x*cos(x),x))




<ol>
<li>
    <p>Use integration by parts:</p>
    <p><script type="math/tex; mode=display">\int \operatorname{u} \operatorname{dv}
                = \operatorname{u}\operatorname{v} -
                \int \operatorname{v} \operatorname{du}</script></p>
    <p>Let <script type="math/tex; mode=inline">u{\left (x \right )} = x</script> and let <script type="math/tex; mode=inline">\operatorname{dv}{\left (x \right )} = \cos{\left (x \right )}</script>.</p>
    <p>Then <script type="math/tex; mode=inline">\operatorname{du}{\left (x \right )} = 1</script>.</p>
    <p>To find <script type="math/tex; mode=inline">v{\left (x \right )}</script>:</p>
    <ol>
    <li>
        <p>The integral of cosine is sine:</p>
        <p><script type="math/tex; mode=display">\int \cos{\left (x \right )}\, dx = \sin{\left (x \right )}</script></p>
    </li>
    </ol>
    <p>Now evaluate the sub-integral.</p>
<li>
    <p>The integral of sine is negative cosine:</p>
    <p><script type="math/tex; mode=display">\int \sin{\left (x \right )}\, dx = - \cos{\left (x \right )}</script></p>
</li>
</li>
<li>
    <p>Add the constant of integration:</p>
    <p><script type="math/tex; mode=display">x \sin{\left (x \right )} + \cos{\left (x \right )}+ \mathrm{constant}</script></p>
</li>
</ol>
<hr/>
<p>The answer is:</p>
<p><script type="math/tex; mode=display">x \sin{\left (x \right )} + \cos{\left (x \right )}+ \mathrm{constant}</script></p>



## Use two times integral by part


    HTML(print_html_steps(x**2*exp(x),x))




<ol>
<li>
    <p>Use integration by parts:</p>
    <p><script type="math/tex; mode=display">\int \operatorname{u} \operatorname{dv}
                = \operatorname{u}\operatorname{v} -
                \int \operatorname{v} \operatorname{du}</script></p>
    <p>Let <script type="math/tex; mode=inline">u{\left (x \right )} = x^{2}</script> and let <script type="math/tex; mode=inline">\operatorname{dv}{\left (x \right )} = e^{x}</script>.</p>
    <p>Then <script type="math/tex; mode=inline">\operatorname{du}{\left (x \right )} = 2 x</script>.</p>
    <p>To find <script type="math/tex; mode=inline">v{\left (x \right )}</script>:</p>
    <ol>
    <li>
        <p>The integral of the exponential function is itself.</p>
        <p><script type="math/tex; mode=display">\int e^{x}\, dx = e^{x}</script></p>
    </li>
    </ol>
    <p>Now evaluate the sub-integral.</p>
<li>
    <p>Use integration by parts:</p>
    <p><script type="math/tex; mode=display">\int \operatorname{u} \operatorname{dv}
                = \operatorname{u}\operatorname{v} -
                \int \operatorname{v} \operatorname{du}</script></p>
    <p>Let <script type="math/tex; mode=inline">u{\left (x \right )} = 2 x</script> and let <script type="math/tex; mode=inline">\operatorname{dv}{\left (x \right )} = e^{x}</script>.</p>
    <p>Then <script type="math/tex; mode=inline">\operatorname{du}{\left (x \right )} = 2</script>.</p>
    <p>To find <script type="math/tex; mode=inline">v{\left (x \right )}</script>:</p>
    <ol>
    <li>
        <p>The integral of the exponential function is itself.</p>
        <p><script type="math/tex; mode=display">\int e^{x}\, dx = e^{x}</script></p>
    </li>
    </ol>
    <p>Now evaluate the sub-integral.</p>
<li>
    <p>The integral of a constant times a function is the constant times the integral of the function:</p>
    <p><script type="math/tex; mode=display">\int 2 e^{x}\, dx = 2 \int e^{x}\, dx</script></p>
    <ol>
    <li>
        <p>The integral of the exponential function is itself.</p>
        <p><script type="math/tex; mode=display">\int e^{x}\, dx = e^{x}</script></p>
    </li>
    </ol>
    <p>So, the result is: <script type="math/tex; mode=inline">2 e^{x}</script></p>
</li>
</li>
</li>
<li>
    <p>Now simplify:</p>
    <p><script type="math/tex; mode=display">\left(x^{2} - 2 x + 2\right) e^{x}</script></p>
</li>
<li>
    <p>Add the constant of integration:</p>
    <p><script type="math/tex; mode=display">\left(x^{2} - 2 x + 2\right) e^{x}+ \mathrm{constant}</script></p>
</li>
</ol>
<hr/>
<p>The answer is:</p>
<p><script type="math/tex; mode=display">\left(x^{2} - 2 x + 2\right) e^{x}+ \mathrm{constant}</script></p>



## A tricky example


    HTML(print_html_steps(expand_trig(sin(3*x)*exp(x)),x))




<ol>
<li>
    <p>Rewrite the integrand:</p>
    <p><script type="math/tex; mode=display">\left(- 4 \sin^{3}{\left (x \right )} + 3 \sin{\left (x \right )}\right) e^{x} = - 4 e^{x} \sin^{3}{\left (x \right )} + 3 e^{x} \sin{\left (x \right )}</script></p>
<li>
    <p>Integrate term-by-term:</p>
    <ol>
    <li>
        <p>The integral of a constant times a function is the constant times the integral of the function:</p>
        <p><script type="math/tex; mode=display">\int - 4 e^{x} \sin^{3}{\left (x \right )}\, dx = - 4 \int e^{x} \sin^{3}{\left (x \right )}\, dx</script></p>
        <ol>
        <li>
            <p>Don't know the steps in finding this integral.</p>
            <p>But the integral is</p>
            <p><script type="math/tex; mode=display">\frac{2 e^{x}}{5} \sin^{3}{\left (x \right )} - \frac{3 e^{x}}{5} \sin^{2}{\left (x \right )} \cos{\left (x \right )} + \frac{3 e^{x}}{10} \sin{\left (x \right )} \cos^{2}{\left (x \right )} - \frac{3 e^{x}}{10} \cos^{3}{\left (x \right )}</script></p>
        </li>
        </ol>
        <p>So, the result is: <script type="math/tex; mode=inline">- \frac{8 e^{x}}{5} \sin^{3}{\left (x \right )} + \frac{12 e^{x}}{5} \sin^{2}{\left (x \right )} \cos{\left (x \right )} - \frac{6 e^{x}}{5} \sin{\left (x \right )} \cos^{2}{\left (x \right )} + \frac{6 e^{x}}{5} \cos^{3}{\left (x \right )}</script></p>
    </li>
    </ol>
    <ol>
    <li>
        <p>The integral of a constant times a function is the constant times the integral of the function:</p>
        <p><script type="math/tex; mode=display">\int 3 e^{x} \sin{\left (x \right )}\, dx = 3 \int e^{x} \sin{\left (x \right )}\, dx</script></p>
        <ol>
        <li>
            <p>Use integration by parts, noting that the integrand eventually repeats itself.</p>
            <ol>
            <li>
                <p>For the integrand <script type="math/tex; mode=inline">e^{x} \sin{\left (x \right )}</script>:</p>
                <p>Let <script type="math/tex; mode=inline">u{\left (x \right )} = \sin{\left (x \right )}</script> and let <script type="math/tex; mode=inline">\operatorname{dv}{\left (x \right )} = e^{x}</script>.</p>
                <p>Then <script type="math/tex; mode=inline">\int e^{x} \sin{\left (x \right )}\, dx = e^{x} \sin{\left (x \right )} - \int e^{x} \cos{\left (x \right )}\, dx</script>.</p>
            </li>
            <li>
                <p>For the integrand <script type="math/tex; mode=inline">e^{x} \cos{\left (x \right )}</script>:</p>
                <p>Let <script type="math/tex; mode=inline">u{\left (x \right )} = \cos{\left (x \right )}</script> and let <script type="math/tex; mode=inline">\operatorname{dv}{\left (x \right )} = e^{x}</script>.</p>
                <p>Then <script type="math/tex; mode=inline">\int e^{x} \sin{\left (x \right )}\, dx = e^{x} \sin{\left (x \right )} - e^{x} \cos{\left (x \right )} + \int - e^{x} \sin{\left (x \right )}\, dx</script>.</p>
            </li>
            <li>
                <p>Notice that the integrand has repeated itself, so move it to one side:</p>
                <p><script type="math/tex; mode=display">2 \int e^{x} \sin{\left (x \right )}\, dx = e^{x} \sin{\left (x \right )} - e^{x} \cos{\left (x \right )}</script></p>
                <p>Therefore,</p>
                <p><script type="math/tex; mode=display">\int e^{x} \sin{\left (x \right )}\, dx = \frac{e^{x}}{2} \sin{\left (x \right )} - \frac{e^{x}}{2} \cos{\left (x \right )}</script></p>
            </li>
            </ol>
        </li>
        </ol>
        <p>So, the result is: <script type="math/tex; mode=inline">\frac{3 e^{x}}{2} \sin{\left (x \right )} - \frac{3 e^{x}}{2} \cos{\left (x \right )}</script></p>
    </li>
    </ol>
    <p>The result is: <script type="math/tex; mode=inline">- \frac{8 e^{x}}{5} \sin^{3}{\left (x \right )} + \frac{12 e^{x}}{5} \sin^{2}{\left (x \right )} \cos{\left (x \right )} - \frac{6 e^{x}}{5} \sin{\left (x \right )} \cos^{2}{\left (x \right )} + \frac{3 e^{x}}{2} \sin{\left (x \right )} + \frac{6 e^{x}}{5} \cos^{3}{\left (x \right )} - \frac{3 e^{x}}{2} \cos{\left (x \right )}</script></p>
</li>
</li>
<li>
    <p>Now simplify:</p>
    <p><script type="math/tex; mode=display">\frac{e^{x}}{10} \left(\sin{\left (3 x \right )} - 3 \cos{\left (3 x \right )}\right)</script></p>
</li>
<li>
    <p>Add the constant of integration:</p>
    <p><script type="math/tex; mode=display">\frac{e^{x}}{10} \left(\sin{\left (3 x \right )} - 3 \cos{\left (3 x \right )}\right)+ \mathrm{constant}</script></p>
</li>
</ol>
<hr/>
<p>The answer is:</p>
<p><script type="math/tex; mode=display">\frac{e^{x}}{10} \left(\sin{\left (3 x \right )} - 3 \cos{\left (3 x \right )}\right)+ \mathrm{constant}</script></p>



## Multiple methods example


    HTML(print_html_steps(expand_trig(sin(2*x)*cos(2*x)),x))




<ol>
<li>
    <p>The integral of a constant times a function is the constant times the integral of the function:</p>
    <p><script type="math/tex; mode=display">\int 2 \left(2 \cos^{2}{\left (x \right )} - 1\right) \sin{\left (x \right )} \cos{\left (x \right )}\, dx = 2 \int \left(2 \cos^{2}{\left (x \right )} - 1\right) \sin{\left (x \right )} \cos{\left (x \right )}\, dx</script></p>
    <ol>
    <li>
        <p>There are multiple ways to do this integral.</p>
    <div class="collapsible">
        <h2>Method #1</h2>
        <ol>
        <li>
            <p>Let <script type="math/tex; mode=inline">u = \cos{\left (x \right )}</script>.</p>
            <p>Then let <script type="math/tex; mode=inline">du = - \sin{\left (x \right )} dx</script> and substitute <script type="math/tex; mode=inline">du</script>:</p>
            <p><script type="math/tex; mode=display">\int - 2 u^{3} + u\, du</script></p>
            <ol>
            <li>
                <p>Integrate term-by-term:</p>
                <ol>
                <li>
                    <p>The integral of a constant times a function is the constant times the integral of the function:</p>
                    <p><script type="math/tex; mode=display">\int - 2 u^{3}\, du = - 2 \int u^{3}\, du</script></p>
                    <ol>
                    <li>
                        <p>The integral of <script type="math/tex; mode=inline">u^{n}</script> is <script type="math/tex; mode=inline">\frac{u^{n + 1}}{n + 1}</script> when <script type="math/tex; mode=inline">n \neq -1</script>:</p>
                        <p><script type="math/tex; mode=display">\int u^{3}\, du = \frac{u^{4}}{4}</script></p>
                    </li>
                    </ol>
                    <p>So, the result is: <script type="math/tex; mode=inline">- \frac{u^{4}}{2}</script></p>
                </li>
                </ol>
                <ol>
                <li>
                    <p>The integral of <script type="math/tex; mode=inline">u^{n}</script> is <script type="math/tex; mode=inline">\frac{u^{n + 1}}{n + 1}</script> when <script type="math/tex; mode=inline">n \neq -1</script>:</p>
                    <p><script type="math/tex; mode=display">\int u\, du = \frac{u^{2}}{2}</script></p>
                </li>
                </ol>
                <p>The result is: <script type="math/tex; mode=inline">- \frac{u^{4}}{2} + \frac{u^{2}}{2}</script></p>
            </li>
            </ol>
            <p>Now substitute <script type="math/tex; mode=inline">u</script> back in:</p>
            <p><script type="math/tex; mode=display">- \frac{1}{2} \cos^{4}{\left (x \right )} + \frac{1}{2} \cos^{2}{\left (x \right )}</script></p>
        </li>
        </ol>
    </div>
    <div class="collapsible">
        <h2>Method #2</h2>
        <ol>
        <li>
            <p>Rewrite the integrand:</p>
            <p><script type="math/tex; mode=display">\left(2 \cos^{2}{\left (x \right )} - 1\right) \sin{\left (x \right )} \cos{\left (x \right )} = 2 \sin{\left (x \right )} \cos^{3}{\left (x \right )} - \sin{\left (x \right )} \cos{\left (x \right )}</script></p>
        <li>
            <p>Integrate term-by-term:</p>
            <ol>
            <li>
                <p>The integral of a constant times a function is the constant times the integral of the function:</p>
                <p><script type="math/tex; mode=display">\int 2 \sin{\left (x \right )} \cos^{3}{\left (x \right )}\, dx = 2 \int \sin{\left (x \right )} \cos^{3}{\left (x \right )}\, dx</script></p>
                <ol>
                <li>
                    <p>Let <script type="math/tex; mode=inline">u = \cos{\left (x \right )}</script>.</p>
                    <p>Then let <script type="math/tex; mode=inline">du = - \sin{\left (x \right )} dx</script> and substitute <script type="math/tex; mode=inline">- du</script>:</p>
                    <p><script type="math/tex; mode=display">\int - u^{3}\, du</script></p>
                    <ol>
                    <li>
                        <p>The integral of a constant times a function is the constant times the integral of the function:</p>
                        <p><script type="math/tex; mode=display">\int - u^{3}\, dx = - \int u^{3}\, dx</script></p>
                        <ol>
                        <li>
                            <p>The integral of <script type="math/tex; mode=inline">u^{n}</script> is <script type="math/tex; mode=inline">\frac{u^{n + 1}}{n + 1}</script> when <script type="math/tex; mode=inline">n \neq -1</script>:</p>
                            <p><script type="math/tex; mode=display">\int u^{3}\, du = \frac{u^{4}}{4}</script></p>
                        </li>
                        </ol>
                        <p>So, the result is: <script type="math/tex; mode=inline">- \frac{u^{4}}{4}</script></p>
                    </li>
                    </ol>
                    <p>Now substitute <script type="math/tex; mode=inline">u</script> back in:</p>
                    <p><script type="math/tex; mode=display">- \frac{1}{4} \cos^{4}{\left (x \right )}</script></p>
                </li>
                </ol>
                <p>So, the result is: <script type="math/tex; mode=inline">- \frac{1}{2} \cos^{4}{\left (x \right )}</script></p>
            </li>
            </ol>
            <ol>
            <li>
                <p>The integral of a constant times a function is the constant times the integral of the function:</p>
                <p><script type="math/tex; mode=display">\int - \sin{\left (x \right )} \cos{\left (x \right )}\, dx = - \int \sin{\left (x \right )} \cos{\left (x \right )}\, dx</script></p>
                <ol>
                <li>
                    <p>Let <script type="math/tex; mode=inline">u = \cos{\left (x \right )}</script>.</p>
                    <p>Then let <script type="math/tex; mode=inline">du = - \sin{\left (x \right )} dx</script> and substitute <script type="math/tex; mode=inline">- du</script>:</p>
                    <p><script type="math/tex; mode=display">\int - u\, du</script></p>
                    <ol>
                    <li>
                        <p>The integral of a constant times a function is the constant times the integral of the function:</p>
                        <p><script type="math/tex; mode=display">\int - u\, dx = - \int u\, dx</script></p>
                        <ol>
                        <li>
                            <p>The integral of <script type="math/tex; mode=inline">u^{n}</script> is <script type="math/tex; mode=inline">\frac{u^{n + 1}}{n + 1}</script> when <script type="math/tex; mode=inline">n \neq -1</script>:</p>
                            <p><script type="math/tex; mode=display">\int u\, du = \frac{u^{2}}{2}</script></p>
                        </li>
                        </ol>
                        <p>So, the result is: <script type="math/tex; mode=inline">- \frac{u^{2}}{2}</script></p>
                    </li>
                    </ol>
                    <p>Now substitute <script type="math/tex; mode=inline">u</script> back in:</p>
                    <p><script type="math/tex; mode=display">- \frac{1}{2} \cos^{2}{\left (x \right )}</script></p>
                </li>
                </ol>
                <p>So, the result is: <script type="math/tex; mode=inline">\frac{1}{2} \cos^{2}{\left (x \right )}</script></p>
            </li>
            </ol>
            <p>The result is: <script type="math/tex; mode=inline">- \frac{1}{2} \cos^{4}{\left (x \right )} + \frac{1}{2} \cos^{2}{\left (x \right )}</script></p>
        </li>
        </li>
        </ol>
    </div>
    </li>
    </ol>
    <p>So, the result is: <script type="math/tex; mode=inline">- \cos^{4}{\left (x \right )} + \cos^{2}{\left (x \right )}</script></p>
</li>
<li>
    <p>Now simplify:</p>
    <p><script type="math/tex; mode=display">- \frac{1}{8} \cos{\left (4 x \right )} + \frac{1}{8}</script></p>
</li>
<li>
    <p>Add the constant of integration:</p>
    <p><script type="math/tex; mode=display">- \frac{1}{8} \cos{\left (4 x \right )} + \frac{1}{8}+ \mathrm{constant}</script></p>
</li>
</ol>
<hr/>
<p>The answer is:</p>
<p><script type="math/tex; mode=display">- \frac{1}{8} \cos{\left (4 x \right )} + \frac{1}{8}+ \mathrm{constant}</script></p>


