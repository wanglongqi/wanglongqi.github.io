---
author: Longqi
comments: true
date: 2014-11-06 16:15:27
layout: post
slug: Googlevis
title: GoogleVis示例
categories: [R]
tags:
- Tutorial
- R
---
![Matplotlib.chm](https://wanglongqi.github.io/public/images/gvis.png)
[Google Chart api ](https://developers.google.com/chart/) 是一个已经提出很多年的接口了，很多网站都在用，但是Google现在国内被封，估计也没法使用了，这个文章就算为国外的朋友们推荐GoogleVis吧！

Google Chart api （GCA）虽然做得还不错，但是对于我们这类非专业人士还是很麻烦，为了画个图花很长的时间写JS实在是有点本末倒置。不过自从有了googleVis的R程序包之后，你已经不需要再写JS就能得到不错的动态图像了，非常适合在有*互联网*的地方展示各种图像。GCA的缺陷就是没有离线版本，你要拿着个网页倒没有网络的地方，什么都显示不出来。

下面给一个googleVis绘制Bubble图的范例，很简单啦！

{% highlight r %}
library(googleVis)
eng$Status='Intact'
eng[5:6,'Status']='Partial Loose'
eng[7:8,'Status']='Loose'
eng$Status=factor(eng$Status,levels=c('Intact','Partial Loose','Loose'))
op <- options(gvis.plot.tag= 'chart' )
plot(gvisBubbleChart(eng,colorvar="Status",
                     opt=list(height=400,
                              vAxes="[{title:'Index1'}]",
                              hAxes="[{title:'Index2'}]")))
{% endhighlight %}
<!-- BubbleChart generated in R 3.1.2 by googleVis 0.5.6 package -->
<!-- Thu Nov 06 16:50:25 2014 -->


<!-- jsHeader -->
<script type="text/javascript">
 
// jsData 
function gvisDataBubbleChartIDf5c2a463b72 () {
var data = new google.visualization.DataTable();
var datajson =
[
 [
 "exp01",
2.154995034e-05,
0.001213282824,
"Intact" 
],
[
 "exp02",
1.576030116e-05,
0.001000767808,
"Intact" 
],
[
 "exp03",
1.602709602e-05,
0.001047932116,
"Intact" 
],
[
 "exp04",
1.839029082e-05,
0.001098033972,
"Intact" 
],
[
 "exp05",
2.531566803e-06,
0.0003721088572,
"Partial Loose" 
],
[
 "exp06",
1.069058356e-06,
0.0001802606227,
"Partial Loose" 
],
[
 "exp07",
8.64467436e-07,
0.0002069032907,
"Loose" 
],
[
 "exp08",
2.358082007e-06,
0.0003072067572,
"Loose" 
],
[
 "exp09",
1.772299325e-05,
0.001848537574,
"Intact" 
],
[
 "exp10",
1.242288939e-05,
0.001789833268,
"Intact" 
] 
];
data.addColumn('string','x');
data.addColumn('number','Index2');
data.addColumn('number','Index1');
data.addColumn('string','Status');
data.addRows(datajson);
return(data);
}
 
// jsDrawChart
function drawChartBubbleChartIDf5c2a463b72() {
var data = gvisDataBubbleChartIDf5c2a463b72();
var options = {};
options["height"] =    400;
options["vAxes"] = [{title:'Index1'}];
options["hAxes"] = [{title:'Index2'}];


    var chart = new google.visualization.BubbleChart(
    document.getElementById('BubbleChartIDf5c2a463b72')
    );
    chart.draw(data,options);
    

}
  
 
// jsDisplayChart
(function() {
var pkgs = window.__gvisPackages = window.__gvisPackages || [];
var callbacks = window.__gvisCallbacks = window.__gvisCallbacks || [];
var chartid = "corechart";
  
// Manually see if chartid is in pkgs (not all browsers support Array.indexOf)
var i, newPackage = true;
for (i = 0; newPackage && i < pkgs.length; i++) {
if (pkgs[i] === chartid)
newPackage = false;
}
if (newPackage)
  pkgs.push(chartid);
  
// Add the drawChart function to the global list of callbacks
callbacks.push(drawChartBubbleChartIDf5c2a463b72);
})();
function displayChartBubbleChartIDf5c2a463b72() {
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
<script type="text/javascript" src="https://www.google.com/jsapi?callback=displayChartBubbleChartIDf5c2a463b72"></script>
 
<!-- divChart -->
  
<div id="BubbleChartIDf5c2a463b72" 
  style="width: 600; height: 400;">
</div>