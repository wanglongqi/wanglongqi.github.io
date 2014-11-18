---
author: Longqi
comments: true
date: 2014-11-18 11:18:14
layout: post
slug: PygmentShortNames
title: Pygment的语言代号速查表
published: True
categories: [Site]
tags:
- Site
- Pygment
- Python
---
![Python](/public/images/python.png)
Jekyll 可以使用Pygment做语法高亮，格式是

&#123;% highlight 语言代码 %&#125;<br/>
Hello world!<br/>
&#123;% endhighlight %&#125;<br/>

所以需要这个语言代码，帮助里有，很臭很长，所以直接用R重新处理了一下。然后用Google Chart api弄了个表格，当然是用[GoogleVis包弄的]({% post_url 2014-11-06-GoogleVis %})。嗯，下面就是格式和代号对应表了：

<!-- jsHeader -->
<script type="text/javascript">


// jsData 
function gvisDataTableID465052eb1e87 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
 "as3, actionscript3",
"*.as" 
],
[
 "as, actionscript",
"*.as" 
],
[
 "mxml",
"*.mxml" 
],
[
 "gap",
"*.g, *.gd, *.gi, *.gap" 
],
[
 "mathematica, mma, nb",
"*.nb, *.cdf, *.nbp, *.ma" 
],
[
 "mupad",
"*.mu" 
],
[
 "at, ambienttalk, ambienttalk/2",
"*.at" 
],
[
 "apl",
"*.apl" 
],
[
 "c-objdump",
"*.c-objdump" 
],
[
 "ca65",
"*.s" 
],
[
 "cpp-objdump, c++-objdumb, cxx-objdump",
"*.cpp-objdump, *.c++-objdump, *.cxx-objdump" 
],
[
 "d-objdump",
"*.d-objdump" 
],
[
 "gas, asm",
"*.s, *.S" 
],
[
 "llvm",
"*.ll" 
],
[
 "nasm",
"*.asm, *.ASM" 
],
[
 "objdump-nasm",
"*.objdump-intel" 
],
[
 "objdump",
"*.objdump" 
],
[
 "autoit",
"*.au3" 
],
[
 "ahk, autohotkey",
"*.ahk, *.ahkl" 
],
[
 "blitzbasic, b3d, bplus",
"*.bb, *.decls" 
],
[
 "blitzmax, bmax",
"*.bmx" 
],
[
 "cbmbas",
"*.bas" 
],
[
 "monkey",
"*.monkey" 
],
[
 "qbasic, basic",
"*.BAS, *.bas" 
],
[
 "abap",
"*.abap" 
],
[
 "cobolfree",
"*.cbl, *.CBL" 
],
[
 "cobol",
"*.cob, *.COB, *.cpy, *.CPY" 
],
[
 "gooddata-cl",
"*.gdc" 
],
[
 "maql",
"*.maql" 
],
[
 "openedge, abl, progress",
"*.p, *.cls" 
],
[
 "c",
"*.c, *.h, *.idc" 
],
[
 "cpp, c++",
"*.cpp, *.hpp, *.c++, *.h++, *.cc, *.hh, *.cxx, *.hxx, *.C, *.H, *.cp, *.CPP" 
],
[
 "clay",
"*.clay" 
],
[
 "cuda, cu",
"*.cu, *.cuh" 
],
[
 "ec",
"*.ec, *.eh" 
],
[
 "mql, mq4, mq5, mql4, mql5",
"*.mq4, *.mq5, *.mqh" 
],
[
 "nesc",
"*.nc" 
],
[
 "pike",
"*.pike, *.pmod" 
],
[
 "swig",
"*.swg, *.i" 
],
[
 "vala, vapi",
"*.vala, *.vapi" 
],
[
 "chapel, chpl",
"*.chpl" 
],
[
 "apacheconf, aconf, apache",
".htaccess, apache.conf, apache2.conf" 
],
[
 "cfengine3, cf3",
"*.cf" 
],
[
 "docker, dockerfile",
"Dockerfile, *.docker" 
],
[
 "ini, cfg, dosini",
"*.ini, *.cfg" 
],
[
 "kconfig, menuconfig, linux-config, kernel-config",
"Kconfig, *Config.in*, external.in*, standard-modules.in" 
],
[
 "properties, jproperties",
"*.properties" 
],
[
 "registry",
"*.reg" 
],
[
 "squidconf, squid.conf, squid",
"squid.conf" 
],
[
 "pypylog, pypy",
"*.pypylog" 
],
[
 "css",
"*.css" 
],
[
 "sass",
"*.sass" 
],
[
 "scss",
"*.scss" 
],
[
 "croc",
"*.croc" 
],
[
 "d",
"*.d, *.di" 
],
[
 "smali",
"*.smali" 
],
[
 "jsonld, json-ld",
"*.jsonld" 
],
[
 "json",
"*.json" 
],
[
 "yaml",
"*.yaml, *.yml" 
],
[
 "dpatch",
"*.dpatch, *.darcspatch" 
],
[
 "diff, udiff",
"*.diff, *.patch" 
],
[
 "boo",
"*.boo" 
],
[
 "aspx-cs",
"*.aspx, *.asax, *.ascx, *.ashx, *.asmx, *.axd" 
],
[
 "csharp, c#",
"*.cs" 
],
[
 "fsharp",
"*.fs, *.fsi" 
],
[
 "nemerle",
"*.n" 
],
[
 "aspx-vb",
"*.aspx, *.asax, *.ascx, *.ashx, *.asmx, *.axd" 
],
[
 "vb.net, vbnet",
"*.vb, *.bas" 
],
[
 "alloy",
"*.als" 
],
[
 "bro",
"*.bro" 
],
[
 "mscgen, msc",
"*.msc" 
],
[
 "pan",
"*.pan" 
],
[
 "protobuf, proto",
"*.proto" 
],
[
 "puppet",
"*.pp" 
],
[
 "rsl",
"*.rsl" 
],
[
 "vgl",
"*.rpf" 
],
[
 "dylan-console, dylan-repl",
"*.dylan-console" 
],
[
 "dylan",
"*.dylan, *.dyl, *.intr" 
],
[
 "dylan-lid, lid",
"*.lid, *.hdp" 
],
[
 "ecl",
"*.ecl" 
],
[
 "eiffel",
"*.e" 
],
[
 "elixir, ex, exs",
"*.ex, *.exs" 
],
[
 "erlang",
"*.erl, *.hrl, *.es, *.escript" 
],
[
 "erl",
"*.erl-sh" 
],
[
 "befunge",
"*.befunge" 
],
[
 "brainfuck, bf",
"*.bf, *.b" 
],
[
 "redcode",
"*.cw" 
],
[
 "factor",
"*.factor" 
],
[
 "fan",
"*.fan" 
],
[
 "felix, flx",
"*.flx, *.flxh" 
],
[
 "fortran",
"*.f, *.f90, *.F, *.F90" 
],
[
 "foxpro, vfp, clipper, xbase",
"*.PRG, *.prg" 
],
[
 "go",
"*.go" 
],
[
 "cypher",
"*.cyp, *.cypher" 
],
[
 "asy, asymptote",
"*.asy" 
],
[
 "glsl",
"*.vert, *.frag, *.geo" 
],
[
 "gnuplot",
"*.plot, *.plt" 
],
[
 "postscript, postscr",
"*.ps, *.eps" 
],
[
 "pov",
"*.pov, *.inc" 
],
[
 "agda",
"*.agda" 
],
[
 "cryptol, cry",
"*.cry" 
],
[
 "haskell, hs",
"*.hs" 
],
[
 "idris, idr",
"*.idr" 
],
[
 "koka",
"*.kk, *.kki" 
],
[
 "lagda, literate-agda",
"*.lagda" 
],
[
 "lcry, literate-cryptol, lcryptol",
"*.lcry" 
],
[
 "lhs, literate-haskell, lhaskell",
"*.lhs" 
],
[
 "lidr, literate-idris, lidris",
"*.lidr" 
],
[
 "hx, haxe, hxsl",
"*.hx, *.hxsl" 
],
[
 "haxeml, hxml",
"*.hxml" 
],
[
 "systemverilog, sv",
"*.sv, *.svh" 
],
[
 "verilog, v",
"*.v" 
],
[
 "vhdl",
"*.vhdl, *.vhd" 
],
[
 "dtd",
"*.dtd" 
],
[
 "haml",
"*.haml" 
],
[
 "html",
"*.html, *.htm, *.xhtml, *.xslt" 
],
[
 "jade",
"*.jade" 
],
[
 "scaml",
"*.scaml" 
],
[
 "xml",
"*.xml, *.xsl, *.rss, *.xslt, *.xsd, *.wsdl, *.wsf" 
],
[
 "xslt",
"*.xsl, *.xslt, *.xpl" 
],
[
 "idl",
"*.pro" 
],
[
 "igor, igorpro",
"*.ipf" 
],
[
 "limbo",
"*.b" 
],
[
 "control, debcontrol",
"control" 
],
[
 "nsis, nsi, nsh",
"*.nsi, *.nsh" 
],
[
 "spec",
"*.spec" 
],
[
 "sourceslist, sources.list, debsources",
"sources.list" 
],
[
 "inform6, i6",
"*.inf" 
],
[
 "i6t",
"*.i6t" 
],
[
 "inform7, i7",
"*.ni, *.i7x" 
],
[
 "tads3",
"*.t" 
],
[
 "io",
"*.io" 
],
[
 "coffee-script, coffeescript, coffee",
"*.coffee" 
],
[
 "dart",
"*.dart" 
],
[
 "js, javascript",
"*.js" 
],
[
 "kal",
"*.kal" 
],
[
 "lasso, lassoscript",
"*.lasso, *.lasso[89]" 
],
[
 "live-script, livescript",
"*.ls" 
],
[
 "mask",
"*.mask" 
],
[
 "objective-j, objectivej, obj-j, objj",
"*.j" 
],
[
 "ts",
"*.ts" 
],
[
 "julia, jl",
"*.jl" 
],
[
 "aspectj",
"*.aj" 
],
[
 "ceylon",
"*.ceylon" 
],
[
 "clojure, clj",
"*.clj" 
],
[
 "clojurescript, cljs",
"*.cljs" 
],
[
 "golo",
"*.golo" 
],
[
 "gosu",
"*.gs, *.gsx, *.gsp, *.vark" 
],
[
 "gst",
"*.gst" 
],
[
 "groovy",
"*.groovy" 
],
[
 "ioke, ik",
"*.ik" 
],
[
 "jasmin, jasminxt",
"*.j" 
],
[
 "java",
"*.java" 
],
[
 "kotlin",
"*.kt" 
],
[
 "pig",
"*.pig" 
],
[
 "scala",
"*.scala" 
],
[
 "xtend",
"*.xtend" 
],
[
 "common-lisp, cl, lisp, elisp, emacs, emacs-lisp",
"*.cl, *.lisp, *.el" 
],
[
 "hylang",
"*.hy" 
],
[
 "newlisp",
"*.lsp, *.nl" 
],
[
 "racket, rkt",
"*.rkt, *.rktd, *.rktl" 
],
[
 "scheme, scm",
"*.scm, *.ss" 
],
[
 "cmake",
"*.cmake, CMakeLists.txt" 
],
[
 "make, makefile, mf, bsdmake",
"*.mak, *.mk, Makefile, makefile, Makefile.*, GNUmakefile" 
],
[
 "groff, nroff, man",
"*.[1234567], *.man" 
],
[
 "css+mozpreproc",
"*.css.in" 
],
[
 "javascript+mozpreproc",
"*.js.in" 
],
[
 "xul+mozpreproc",
"*.xul.in" 
],
[
 "rst, rest, restructuredtext",
"*.rst, *.rest" 
],
[
 "tex, latex",
"*.tex, *.aux, *.toc" 
],
[
 "matlab",
"*.m" 
],
[
 "octave",
"*.m" 
],
[
 "scilab",
"*.sci, *.sce, *.tst" 
],
[
 "ocaml",
"*.ml, *.mli, *.mll, *.mly" 
],
[
 "opa",
"*.opa" 
],
[
 "sml",
"*.sml, *.sig, *.fun" 
],
[
 "bugs, winbugs, openbugs",
"*.bug" 
],
[
 "jags",
"*.jag, *.bug" 
],
[
 "modelica",
"*.mo" 
],
[
 "stan",
"*.stan" 
],
[
 "nimrod, nim",
"*.nim, *.nimrod" 
],
[
 "nit",
"*.nit" 
],
[
 "nixos, nix",
"*.nix" 
],
[
 "logos",
"*.x, *.xi, *.xm, *.xmi" 
],
[
 "objective-c, objectivec, obj-c, objc",
"*.m, *.h" 
],
[
 "objective-c++, objectivec++, obj-c++, objc++",
"*.mm, *.hh" 
],
[
 "swift",
"*.swift" 
],
[
 "ooc",
"*.ooc" 
],
[
 "antlr-as, antlr-actionscript",
"*.G, *.g" 
],
[
 "antlr-csharp, antlr-c#",
"*.G, *.g" 
],
[
 "antlr-cpp",
"*.G, *.g" 
],
[
 "antlr-java",
"*.G, *.g" 
],
[
 "antlr-objc",
"*.G, *.g" 
],
[
 "antlr-perl",
"*.G, *.g" 
],
[
 "antlr-python",
"*.G, *.g" 
],
[
 "antlr-ruby, antlr-rb",
"*.G, *.g" 
],
[
 "ebnf",
"*.ebnf" 
],
[
 "ragel-c",
"*.rl" 
],
[
 "ragel-cpp",
"*.rl" 
],
[
 "ragel-d",
"*.rl" 
],
[
 "ragel-em",
"*.rl" 
],
[
 "ragel-java",
"*.rl" 
],
[
 "ragel-objc",
"*.rl" 
],
[
 "ragel-ruby, ragel-rb",
"*.rl" 
],
[
 "treetop",
"*.treetop, *.tt" 
],
[
 "ada, ada95, ada2005",
"*.adb, *.ads, *.ada" 
],
[
 "delphi, pas, pascal, objectpascal",
"*.pas" 
],
[
 "modula2, m2",
"*.def, *.mod" 
],
[
 "pawn",
"*.p, *.pwn, *.inc" 
],
[
 "sp",
"*.sp" 
],
[
 "perl6, pl6",
"*.pl, *.pm, *.nqp, *.p6, *.6pl, *.p6l, *.pl6, *.6pm, *.p6m, *.pm6, *.t" 
],
[
 "perl, pl",
"*.pl, *.pm, *.t" 
],
[
 "php, php3, php4, php5",
"*.php, *.php[345], *.inc" 
],
[
 "zephir",
"*.zep" 
],
[
 "logtalk",
"*.lgt, *.logtalk" 
],
[
 "prolog",
"*.ecl, *.prolog, *.pro, *.pl" 
],
[
 "cython, pyx, pyrex",
"*.pyx, *.pxd, *.pxi" 
],
[
 "dg",
"*.dg" 
],
[
 "py3tb",
"*.py3tb" 
],
[
 "python, py, sage",
"*.py, *.pyw, *.sc, SConstruct, SConscript, *.tac, *.sage" 
],
[
 "pytb",
"*.pytb" 
],
[
 "rconsole, rout",
"*.Rout" 
],
[
 "rd",
"*.Rd" 
],
[
 "splus, s, r",
"*.S, *.R, .Rhistory, .Rprofile, .Renviron" 
],
[
 "sparql",
"*.rq, *.sparql" 
],
[
 "rebol",
"*.r, *.r3, *.reb" 
],
[
 "red, red/system",
"*.red, *.reds" 
],
[
 "resource, resourcebundle",
"*.txt" 
],
[
 "robotframework",
"*.txt, *.robot" 
],
[
 "fancy, fy",
"*.fy, *.fancypack" 
],
[
 "rb, ruby, duby",
"*.rb, *.rbw, Rakefile, *.rake, *.gemspec, *.rbx, *.duby" 
],
[
 "rust",
"*.rs" 
],
[
 "applescript",
"*.applescript" 
],
[
 "chai, chaiscript",
"*.chai" 
],
[
 "hybris, hy",
"*.hy, *.hyb" 
],
[
 "lsl",
"*.lsl" 
],
[
 "lua",
"*.lua, *.wlua" 
],
[
 "moocode, moo",
"*.moo" 
],
[
 "moon, moonscript",
"*.moon" 
],
[
 "rexx, arexx",
"*.rexx, *.rex, *.rx, *.arexx" 
],
[
 "bash, sh, ksh, shell",
"*.sh, *.ksh, *.bash, *.ebuild, *.eclass, .bashrc, bashrc, .bash\*, bash\*, PKGBUILD" 
],
[
 "console",
"*.sh-session" 
],
[
 "bat, batch, dosbatch, winbatch",
"*.bat, *.cmd" 
],
[
 "powershell, posh, ps1, psm1",
"*.ps1, *.psm1" 
],
[
 "shell-session",
"*.shell-session" 
],
[
 "tcsh, csh",
"*.tcsh, *.csh" 
],
[
 "newspeak",
"*.ns2" 
],
[
 "smalltalk, squeak, st",
"*.st" 
],
[
 "snobol",
"*.snobol" 
],
[
 "text",
"*.txt" 
],
[
 "rql",
"*.rql" 
],
[
 "sql",
"*.sql" 
],
[
 "sqlite3",
"*.sqlite3-console" 
],
[
 "tcl",
"*.tcl, *.rvt" 
],
[
 "cheetah, spitfire",
"*.tmpl, *.spt" 
],
[
 "cfc",
"*.cfc" 
],
[
 "cfm",
"*.cfm, *.cfml" 
],
[
 "html+evoque",
"*.html" 
],
[
 "evoque",
"*.evoque" 
],
[
 "xml+evoque",
"*.xml" 
],
[
 "genshi, kid, xml+genshi, xml+kid",
"*.kid" 
],
[
 "html+handlebars",
"*.handlebars, *.hbs" 
],
[
 "html+php",
"*.phtml" 
],
[
 "jsp",
"*.jsp" 
],
[
 "liquid",
"*.liquid" 
],
[
 "mako",
"*.mao" 
],
[
 "mason",
"*.m, *.mhtml, *.mc, *.mi, autohandler, dhandler" 
],
[
 "myghty",
"*.myt, autodelegate" 
],
[
 "rhtml, html+erb, html+ruby",
"*.rhtml" 
],
[
 "smarty",
"*.tpl" 
],
[
 "ssp",
"*.ssp" 
],
[
 "tea",
"*.tea" 
],
[
 "html+twig",
"*.twig" 
],
[
 "velocity",
"*.vm, *.fhtml" 
],
[
 "yaml+jinja, salt, sls",
"*.sls" 
],
[
 "cucumber, gherkin",
"*.feature" 
],
[
 "awk, gawk, mawk, nawk",
"*.awk" 
],
[
 "vim",
"*.vim, .vimrc, .exrc, .gvimrc, vimrc, exrc, gvimrc, vimrc, gvimrc" 
],
[
 "pot, po",
"*.pot, *.po" 
],
[
 "irc",
"*.weechatlog" 
],
[
 "todotxt",
"todo.txt, *.todotxt" 
],
[
 "coq",
"*.v" 
],
[
 "isabelle",
"*.thy" 
],
[
 "lean",
"*.lean" 
],
[
 "urbiscript",
"*.u" 
],
[
 "cirru",
"*.cirru" 
],
[
 "duel, jbst, jsonml+bst",
"*.duel, *.jbst" 
],
[
 "qml",
"*.qml" 
],
[
 "slim",
"*.slim" 
],
[
 "xquery, xqy, xq, xql, xqm",
"*.xqy, *.xquery, *.xq, *.xql, *.xqm" 
] 
];
data.addColumn('string','ShortNames');
data.addColumn('string','FileNames');
data.addRows(datajson);
return(data);
}


// jsDrawChart
function drawChartTableID465052eb1e87() {
var data = gvisDataTableID465052eb1e87();
var options = {};
options["allowHtml"] = true;


    var chart = new google.visualization.Table(
    document.getElementById('TableID465052eb1e87')
    );
    chart.draw(data,options);
    

}
  


// jsDisplayChart
(function() {
var pkgs = window.__gvisPackages = window.__gvisPackages || [];
var callbacks = window.__gvisCallbacks = window.__gvisCallbacks || [];
var chartid = "table";
  
// Manually see if chartid is in pkgs (not all browsers support Array.indexOf)
var i, newPackage = true;
for (i = 0; newPackage && i < pkgs.length; i++) {
if (pkgs[i] === chartid)
newPackage = false;
}
if (newPackage)
  pkgs.push(chartid);
  
// Add the drawChart function to the global list of callbacks
callbacks.push(drawChartTableID465052eb1e87);
})();
function displayChartTableID465052eb1e87() {
  var pkgs = window.__gvisPackages = window.__gvisPackages || [];
  var callbacks = window.__gvisCallbacks = window.__gvisCallbacks || [];
  window.clearTimeout(window.__gvisLoad);
  // The timeout is set to 100 because otherwise the container div we are
  // targeting might not be part of the document yet
  window.__gvisLoad = setTimeout(function() {
  var pkgCount = pkgs.length;
  google.load("visualization", "1", { packages:pkgs, callback: function() {
  if (pkgCount != pkgs.length) {
  // Race condition where another setTimeout call snuck in after us; if
  // that call added a package, we must not shift its callback
  return;
}
while (callbacks.length > 0)
callbacks.shift()();
} });
}, 100);
}


// jsFooter
</script>


<!-- jsChart -->  
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartTableID465052eb1e87"></script>


<!-- divChart -->
  
<div id="TableID465052eb1e87" 
  style="width: 500; height: automatic;">
</div>

