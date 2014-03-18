---
author: Longqi
comments: true
date: 2017-03-15 15:37:06 +0800
layout: post
slug: aboutindiarape
title: 打假：印度是强奸之国
categories: [R]
tags:
-  R
-  Statistics
-  Tutorial
---
<script src="/public/js/jquery-1.12.4/jquery.min.js"></script>
<script src="/public/js/navigation-1.1/tabsets.js"></script>
<link href="/public/js/highlightjs-1.1/default.css" rel="stylesheet" />
<script src="/public/js/highlightjs-1.1/highlight.js"></script>
<script src="/public/js/htmlwidgets-0.8/htmlwidgets.js"></script>
<script src="/public/js/datatables-binding-0.2/datatables.js"></script>
<link href="/public/js/dt-core-1.10.12/css/jquery.dataTables.min.css" rel="stylesheet" />
<link href="/public/js/dt-core-1.10.12/css/jquery.dataTables.extra.css" rel="stylesheet" />
<script src="/public/js/dt-core-1.10.12/js/jquery.dataTables.min.js"></script>
<link href="/public/js/nouislider-7.0.10/jquery.nouislider.min.css" rel="stylesheet" />
<script src="/public/js/nouislider-7.0.10/jquery.nouislider.min.js"></script>
<script src="/public/js/selectize-0.12.0/selectize.min.js"></script>
<div class="section level2">
<h2>背景</h2>
<p>今天又看到有人吐槽印度是强奸之国，想想上次这事发酵的时候到现在已经快半年了，当时很多很有“知名度”的节目也是吐槽一地。其实我和乙寅当时就很奇怪印度官员既然已经给出了一组明确的数据，为什么没有人去考察相关的数据，而是直接就上来一顿嘲讽。下面让我们来回顾一下这个事件吧。在网上随便都能搜到那个事件的导火索，比如<a href="http://www.ettoday.net/news/20161124/816863.htm">印度官員：性侵案數量其實全球前四低</a>，<a href="http://news.ltn.com.tw/news/world/breakingnews/1896058">印度官員：印度強姦案數是世界最低4個國家之一</a>或者来自搜狐的<a href="http://news.sohu.com/20161123/n473937606.shtml">印度女部长：印度属于强奸案最低4个国家之一</a>，大致内容是：</p>
<blockquote>
<p>印度婦女及兒童發展部的女部長馬內卡‧甘地（Maneka Gandhi）週一（21日）舉行一場女記者聚會，她在會中表示，印度的強姦案件數量，是世界上最低的4個國家之一，瑞典的案發數第一。</p>
</blockquote>
<p>然后网上就出来了各种讨伐文章，在这里列举几个，网上要找的话可谓不一而足。</p>
<p>比如，来自搜狐的： <a href="http://star.news.sohu.com/20161124/n474063275.shtml">网友快评：印度强奸案发生率最低 我差点就信了</a></p>
<p>这个好像还查过资料一样，其中内容不乏：</p>
<blockquote>
<p>她说的没有错吧，人家说的强奸率，人家人口基数大啊，一天一万起强奸除以十四亿貌似也只是个小数</p>
</blockquote>
<blockquote>
<p>替瑞典喊冤“瑞典政府和人民无辜躺枪。</p>
</blockquote>
<blockquote>
<p>总算知道印度为啥是强奸大国了，因为连那里的女人都不把强奸当回事</p>
</blockquote>
<p>其实关于印度是强奸之国的论断很早就有，这里是一个看起来很严肃，做过仔细调研的<a href="http://view.news.qq.com/zt2013/busrape/index.htm">印度如何沦为&quot;强奸之国&quot;</a>文章，其中不乏煽动性的数字：</p>
<blockquote>
<p>数据也证实了这点，根据印度国家犯罪记录局的数据，印度记录在案的强奸案件由1971年的2487起增至2011年的24206起，增长率为873.3%。比较而言，谋杀案件在从1953至2011年的近60年间里的增长率为250%，远不及强奸犯罪率的飙升。 平均下来，在印度每3分钟发生一起针对女性的暴力犯罪，每22分钟就会发生一起强奸案。在印度性犯罪最严重的主要城市新德里，平均每18小时发生一起强奸案，被冠以 “强奸之都”的耻辱称号。</p>
</blockquote>
<p>按照一般的理解，作为一个国家的高级官员，说话完全不着边际的可能性是不大的，特别是还列举<strong>明确数据</strong>的话语。但是如果你真的去查的话，很容易找到的一个条目是<a href="https://zh.wikipedia.org/wiki/强奸">中文维基百科的条目</a>，不过不用太多的分析就应该可以发现那个页面的数据是错误的（这个大家自己去分析吧）。所以，我就稍微多检索了一下，很快就能发现联合国药物与犯罪部门公布了性犯罪的<a href="https://stats.unodc.org/webcontent/dcm.uploads/downloads/Publication%20Reports_1a.xlsx">相关信息</a>。很容易核对这个表格中的数据和上面文章提供的数据是基本吻合的，应该说也是比较可信的。</p>
</div>
<div class="section level2">
<h2>分析方法</h2>
<p>考虑到不同的国家人口差异比较大，使用每十万人的案件发生数量是比较合理的选择。而像中文维基页面中使用所谓的一个国家每分钟的的案发次数是并不合理的。正是上面说的“人家人口基数大啊，一天一万起强奸除以十四亿貌似也只是个小数”，这话虽然是明显的讽刺，但是确实不加，如果是“一天一千起强奸除以一亿”，不知道这个发言者真的觉得前者比较危险吗？所以我们以下分析的都是每十万人在一年内发生强奸案例的数据。</p>
<p>同时，不同地区之间性犯罪案件的发生件数和登记在案的发生次数也是存在差异的。这一点并不假，特别是在具有“传统美德”的某些国家这个数目更是可能不算小数。但是无疑对于真实的犯案数量和报案数量之间的差异的估计是非常困难的，一个可行的方案可能是认为地理位置和文化相近的区域的这一比例也比较接近。同时，在没有可靠数据的支撑条件下，我们也不应过分夸大这一比例在不同区域的差距。下面让我们开始真正的分析吧！</p>
</div>
<div class="section level2">
<h2>均值分析</h2>
<p>作为标准的分析的第一步，我们先看一下全球的平均水平。几点特征可以注意到，首先每年数据的均值都远过于中位数，其次标准差（SD）对于给定也数据很大，最后整个均值特征量基本是稳定的，没有明显的增长或降低趋势。平均罪案率大概在万分之一。</p>
<pre class="r"><code>globalmean &lt;- rape %&gt;% 
  group_by(Year) %&gt;% 
  summarise(mean=round(mean(Events,na.rm=T),2),
            median=median(Events,na.rm=T),
            sd=round(sd(Events,na.rm=T),2))

datatable(globalmean,options = list(pageLength=20))</code></pre>
<div id="htmlwidget-864ce885c5dee115fc2a" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-864ce885c5dee115fc2a">{"x":{"filter":"none","data":[["1","2","3","4","5","6","7","8","9","10","11","12"],["2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"],[9.83,11.33,9.82,9.9,10.74,9.93,11.02,10.33,11.61,10.49,10.45,10.73],[5.3,5.6,5.2,5.75,5.25,4.95,4.8,5.2,6,5.8,6.2,5.7],[12.86,14.81,11.76,10.35,13.96,12.83,15.4,13.13,14.26,11.34,11.56,15.21]],"container":"<table class=\"display\">\n  <thead>\n    <tr>\n      <th> <\/th>\n      <th>Year<\/th>\n      <th>mean<\/th>\n      <th>median<\/th>\n      <th>sd<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"pageLength":20,"columnDefs":[{"className":"dt-right","targets":[2,3,4]},{"orderable":false,"targets":0}],"order":[],"autoWidth":false,"orderClasses":false,"lengthMenu":[10,20,25,50,100]}},"evals":[],"jsHooks":[]}</script>
<p>简单的将以上数据绘图，颜色偏棕的年份方差比较大。</p>
<pre class="r"><code>p &lt;- ggplot(globalmean,aes(Year,mean,fill=sd))+geom_bar(stat=&quot;identity&quot;)+ 
  scale_fill_distiller(palette = &quot;BrBG&quot;) +
  ylab(&quot;Mean Value&quot;) 
p</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-2-1.png" width="768" /></p>
</div>
<div class="section level2">
<h2>分布分析</h2>
<p>第二步，我们考察一下各年的具体分布情况。首先是用boxplot来看一下离群值的情况。可以看到每年都有一些很大的离群值。</p>
<pre class="r"><code>p &lt;- ggplot(rape,aes(Year,Events,fill=Year)) +
  theme(legend.position = &quot;none&quot;) +
  scale_fill_brewer(palette = &quot;Paired&quot;)

ggplotly(p + geom_boxplot(na.rm = T))</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-3-1.png" width="768" /></p>
<p>boxplot不能看出分布，所以我们使用violinplot来查看一下每年的分布情况：</p>
<pre class="r"><code>p2 &lt;- p + geom_violin(na.rm = T)
ggplotly(p2)</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-4-1.png" width="768" /></p>
</div>
<div class="section level2">
<h2>印度在分布图中的位置</h2>
<p>好的，然后如果我们把印度的位置用<code>+</code>标识在上面的图中会是什么位置呢？</p>
<pre class="r"><code>pindia &lt;- p2 +
  geom_point(data = rape %&gt;% filter(Country==&quot;India&quot;),shape=3,size=5,color=&quot;darkblue&quot;) + scale_fill_brewer(palette = &quot;Paired&quot;)</code></pre>
<pre><code>## Scale for &#39;fill&#39; is already present. Adding another scale for &#39;fill&#39;,
## which will replace the existing scale.</code></pre>
<pre class="r"><code>ggplotly(pindia)</code></pre>
<pre><code>## Warning: Removed 2 rows containing missing values (geom_point).</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-5-1.png" width="768" /></p>
<p>实际上，你需要缩放到10以下，才能看到印度的案件发生率。至少从这个图上来看，来自印度的消息似乎不是毫无根据，而是空穴来风。那么让我们继续分析这个数据。</p>
<pre class="r"><code>pindia +  ylim(0,10)</code></pre>
<pre><code>## Warning: Removed 2 rows containing missing values (geom_point).</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-6-1.png" width="768" /></p>
</div>
<div class="section level2">
<h2>各大洲的情况</h2>
<p>将原始数据按照各大洲的情况分组统计可以得到如下的结果。从结果来看，似乎大洋洲是一个令人恐怖的所在。</p>
<pre class="r"><code>p &lt;- ggplot(rape,aes(Region, Events, fill = Region)) +
  geom_violin(na.rm=T) +
  scale_fill_brewer(palette = &quot;Paired&quot;)
ggplotly(p)</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-7-1.png" width="768" /></p>
<p>对于数据爱好者，我也提供一下数据吧：</p>
<pre class="r"><code>globalmean &lt;- rape %&gt;% 
  group_by(Region) %&gt;% 
  summarise(mean=round(mean(Events,na.rm=T),2),
            median=median(Events,na.rm=T),
            sd=round(sd(Events,na.rm=T),2))

knitr::kable(globalmean)</code></pre>
<table>
<thead>
<tr class="header">
<th align="left">Region</th>
<th align="right">mean</th>
<th align="right">median</th>
<th align="right">sd</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Africa</td>
<td align="right">10.66</td>
<td align="right">2.60</td>
<td align="right">22.43</td>
</tr>
<tr class="even">
<td align="left">Americas</td>
<td align="right">19.30</td>
<td align="right">18.80</td>
<td align="right">12.74</td>
</tr>
<tr class="odd">
<td align="left">Asia</td>
<td align="right">3.92</td>
<td align="right">2.50</td>
<td align="right">4.15</td>
</tr>
<tr class="even">
<td align="left">Europe</td>
<td align="right">9.33</td>
<td align="right">5.60</td>
<td align="right">10.54</td>
</tr>
<tr class="odd">
<td align="left">Oceania</td>
<td align="right">24.31</td>
<td align="right">26.25</td>
<td align="right">7.87</td>
</tr>
</tbody>
</table>
<p>如果我们继续细分分类的话，会出现下面这张不美观的图片。不过，大家可以移动鼠标去查看每个部分代表具体数据。可以看到总体数据来讲，南非区域是鹤立鸡群地高呀！这个大概和平常的新闻媒体传播还是比较吻合的。</p>
<pre class="r"><code>orape &lt;- rape
rape$Country &lt;- unlist(lapply(rape$Country, function(x) substr(x,1,10)))

ggplotly(ggplot(rape,aes(`Sub Region`, Events, fill = `Sub Region`)) +
           theme(legend.position = &quot;none&quot;,
                  axis.text.x = element_text(vjust = 0.25,angle = 90)) +
  geom_violin(na.rm=T) )</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-9-1.png" width="768" /></p>
</div>
<div class="section level2">
<h2>亚洲地区的数据</h2>
<p>好了，我们就不去研究非洲的问题。回来看看亚洲地区的数据吧！这亚洲的国家数量真是很大，大家只能移动鼠标去查看每个数据块对应哪个国家了。几点观察是明显的：</p>
<ol style="list-style-type: decimal">
<li>作为发达国家，日本的罪案率很低。</li>
<li>印度在亚洲国家中也算罪案率不高的。也就是考虑到亚洲地区记录在案的犯罪比例可能偏低，那么在同一地区而言，印度的记录也不算很高。比如附近的泰国罪案率就远高于印度。虽然对于印度及其周边国家的文化并不了解，不过认为印度的罪案记录率又远低于周边地区的话似乎也不是很有道理的假设。</li>
<li>邻国蒙古亮了。</li>
</ol>
<pre class="r"><code>p &lt;- ggplot(rape %&gt;% 
         filter(Region==&quot;Asia&quot;),
       aes(Country, Events, fill = Country)) +
           theme(legend.position = &quot;none&quot;,
                 axis.text.x = element_text(vjust = 0.25,angle = 90)) +
  geom_violin(na.rm=T)
ggplotly(p)</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-10-1.png" width="768" /></p>
</div>
<div class="section level2">
<h2>欧洲地区的数据</h2>
<p>考察欧洲主要是因为之前谣言的对手是欧洲的。可以看到，欧洲里瑞典（Sweden）可谓一枝独秀。</p>
<pre class="r"><code>p &lt;- ggplot(rape %&gt;% 
         filter(Region==&quot;Europe&quot;),
       aes(Country, Events, fill = Country)) +
           theme(legend.position = &quot;none&quot;,
                 axis.text.x = element_text(vjust = 0.25,angle = 90)) +
  geom_violin(na.rm=T)
ggplotly(p)</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-11-1.png" width="768" /></p>
<p>让我们放大到北欧看看，无疑确实瑞典是很高。</p>
<pre class="r"><code>p &lt;- ggplot(rape %&gt;% 
         filter(`Sub Region`==&quot;Northern Europe&quot;),
       aes(Country, Events, fill = Country)) +
           theme(legend.position = &quot;none&quot;,
                 axis.text.x = element_text(vjust = 0.25,angle = 90)) +
  geom_violin(na.rm=T)
ggplotly(p)</code></pre>
<p><img src="/public/images/indiarape/unnamed-chunk-12-1.png" width="768" /></p>
<p>可以观察到， 北欧的罪案率普遍偏高。这一点确实和欧美文化有关，很大程度上欧美的罪案更大可能性会被记录在案，但是这同是北欧（这个地区的文化好像差异不大），瑞典的这个数据实在是让人比较难堪了。同时，这个基准值大家可以记录下来，到时候可以去数据表格中查看类似文化国家的罪案率怎么样，我就不做分析了。默默的在最后附上了各国的罪案发生均值和中位数，以供大家研究。</p>
<p>最后据最高人民法院的消息，去年中国各级法院审结的拐卖、性侵妇女儿童案合计5335件，照此可以估计大概的罪案率情况，这个交给大家吧。</p>
</div>
<div class="section level2">
<h2>各国的数据</h2>
<pre class="r"><code>datatable(orape %&gt;% group_by(Country) %&gt;% 
  summarise(Mean=round(mean(Events,na.rm=T),2),
            Median=round(median(Events,na.rm=T),2),
            SD=round(sd(Events,na.rm=T),2)) %&gt;% 
    arrange(desc(Mean)),filter=&quot;top&quot;,options = list(pageLength=25))</code></pre>
<div id="htmlwidget-ecd882baa3c24726f681" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-ecd882baa3c24726f681">{"x":{"filter":"top","filterHTML":"<tr>\n  <td><\/td>\n  <td data-type=\"character\" style=\"vertical-align: top;\">\n    <div class=\"form-group has-feedback\" style=\"margin-bottom: auto;\">\n      <input type=\"search\" placeholder=\"All\" class=\"form-control\" style=\"width: 100%;\"/>\n      <span class=\"glyphicon glyphicon-remove-circle form-control-feedback\"><\/span>\n    <\/div>\n  <\/td>\n  <td data-type=\"number\" style=\"vertical-align: top;\">\n    <div class=\"form-group has-feedback\" style=\"margin-bottom: auto;\">\n      <input type=\"search\" placeholder=\"All\" class=\"form-control\" style=\"width: 100%;\"/>\n      <span class=\"glyphicon glyphicon-remove-circle form-control-feedback\"><\/span>\n    <\/div>\n    <div style=\"display: none; position: absolute; width: 200px;\">\n      <div data-min=\"0\" data-max=\"92.13\" data-scale=\"2\"><\/div>\n      <span style=\"float: left;\"><\/span>\n      <span style=\"float: right;\"><\/span>\n    <\/div>\n  <\/td>\n  <td data-type=\"number\" style=\"vertical-align: top;\">\n    <div class=\"form-group has-feedback\" style=\"margin-bottom: auto;\">\n      <input type=\"search\" placeholder=\"All\" class=\"form-control\" style=\"width: 100%;\"/>\n      <span class=\"glyphicon glyphicon-remove-circle form-control-feedback\"><\/span>\n    <\/div>\n    <div style=\"display: none; position: absolute; width: 200px;\">\n      <div data-min=\"0\" data-max=\"91.9\" data-scale=\"2\"><\/div>\n      <span style=\"float: left;\"><\/span>\n      <span style=\"float: right;\"><\/span>\n    <\/div>\n  <\/td>\n  <td data-type=\"number\" style=\"vertical-align: top;\">\n    <div class=\"form-group has-feedback\" style=\"margin-bottom: auto;\">\n      <input type=\"search\" placeholder=\"All\" class=\"form-control\" style=\"width: 100%;\"/>\n      <span class=\"glyphicon glyphicon-remove-circle form-control-feedback\"><\/span>\n    <\/div>\n    <div style=\"display: none; position: absolute; width: 200px;\">\n      <div data-min=\"0\" data-max=\"26.32\" data-scale=\"2\"><\/div>\n      <span style=\"float: left;\"><\/span>\n      <span style=\"float: right;\"><\/span>\n    <\/div>\n  <\/td>\n<\/tr>","data":[["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137"],["Lesotho","Botswana","Swaziland","Sweden","St. Vincent and the Grenadines","Suriname","Zimbabwe","Costa Rica","St. Kitts and Nevis","United States of America*","United Kingdom (England and Wales)","Belgium","Jamaica","Bahamas","Nicaragua","New Zealand","Grenada","Guyana","United Kingdom (Northern Ireland)","Panama*","Peru","Barbados","Iceland","Cabo Verde","Bermuda","Bolivia (Plurinational State of)","United Kingdom (Scotland)*","Paraguay","Norway","Trinidad and Tobago","Chile","Brazil","Solomon Islands","Israel","France*","Honduras","Finland","Republic of Korea","Mongolia","Mexico*","Luxembourg","Ecuador","Belize","Kazakhstan","Netherlands*","Ireland","Estonia","Germany","Austria","Dominican Republic","Sri Lanka","Colombia","Burundi","Argentina","Bangladesh","Denmark","Switzerland*","Republic of Moldova","Uruguay","Brunei Darussalam","El Salvador*","Bhutan","Lithuania","Oman","Monaco","Czech Republic","Liechtenstein","Kyrgyzstan","Latvia","Thailand*","Kuwait","Romania*","Macao Special Administrative Region of China*","Poland","Mauritius","Philippines","Russian Federation","Croatia","Spain","Bulgaria","Lebanon","Morocco","Sudan","Portugal","Andorra","Senegal","Malta*","Slovenia","Guatemala","Singapore","Rwanda","Slovakia","Cyprus","Cameroon*","Belarus","Bahrain","Kenya","Hungary","Uganda","Georgia","The former Yugoslav Rep. of Macedonia","Turkey","Sao Tome and Principe","Sierra Leone","Kosovo under UNSCR 1244","Ukraine","India","Jordan","Greece","Maldives","Qatar","Canada*","Hong Kong Special Administrative Region of China","Puerto Rico*","Algeria*","State of Palestine","Albania","Montenegro","Japan","United Arab Emirates","Bosnia and Herzegovina","Serbia","Guinea","Indonesia","Nigeria","Nepal","Tajikistan","Turkmenistan","Syrian Arab Republic","Myanmar","Yemen","Armenia","Azerbaijan","Mozambique","Egypt","Holy See","Iraq (Central Iraq)"],[92.13,89.05,74.85,50.84,46.58,41.85,33.85,33.18,31.83,30.97,29.32,29.13,28.68,28.55,28.17,27.71,27.16,25.28,25.21,24.98,24.48,24.08,23.66,23.65,22.76,21.76,21.09,20.2,19.56,19.36,18.68,18.45,18.18,17.36,16.78,16.73,14.86,12.95,12.87,12.62,12.36,11.8,11.26,10.88,10.85,10.14,9.72,9.68,9.49,9.25,8.64,8.33,8.26,8.22,8,7.72,7.71,7.46,7.37,7.1,6.89,6.78,6.34,6,5.9,5.84,5.77,5.69,5.47,5.29,4.73,4.66,4.61,4.59,4.57,4.46,4.32,4.19,3.97,3.8,3.61,3.56,3.5,3.43,3.35,3.3,3.22,3.19,3.16,2.87,2.85,2.84,2.75,2.7,2.68,2.62,2.62,2.59,2.41,2.26,2.23,2.18,2,1.95,1.91,1.9,1.86,1.75,1.72,1.71,1.7,1.62,1.48,1.4,1.31,1.22,1.2,1.15,1.14,1.14,0.96,0.92,0.9,0.87,0.8,0.75,0.72,0.7,0.67,0.66,0.62,0.36,0.35,0.27,0.08,0,null],[91.9,89.25,74.85,55.75,49.4,41.85,36.35,33.1,30.9,31.15,27.15,29.55,26.5,27.8,28,27,25.95,31.8,24.55,24.15,24.3,24.4,23.9,23.35,9.6,20.9,18.45,21.4,19.9,18.7,18.4,18.9,13.9,18.4,16.45,13.5,14.6,12.95,12.65,12.6,13,11.15,9.6,10.2,10.8,9.65,9.75,9.5,9.3,9.25,8.35,7.6,7.5,8.25,8,7.7,7.65,7.1,6.7,7.1,6.15,7.35,6.15,6,5.8,6,5.6,5.7,4.05,5.55,4.65,4.6,4.6,4.45,4.6,3.7,3.8,3.75,3.9,3.15,3.7,3.6,3.5,3.5,2.4,3.05,3,2.85,2.8,2.75,2.7,2.8,3,3,2.4,2.7,2.3,2.4,2.05,2,2,2.4,1.45,1.95,1.8,1.95,1.8,1.75,1.65,1.6,1.7,1.65,1.5,1.2,1.1,0.4,1.3,0.95,1.15,1.2,0.95,0.9,0.9,0.8,0.8,0.75,0.8,0.7,0.65,0.7,0.6,0.4,0.3,0.2,0.1,0,null],[2.96,2.72,3.75,13.85,18.86,5.3,5.86,2.79,3.69,3.15,7.61,1.5,3.29,6.13,3.65,2.52,8.35,12.56,4.68,3.92,3.36,3.84,3.41,2.38,26.32,7.42,6.1,2.44,2.38,3.92,1.5,4.81,10.76,2.58,0.9,5.86,3.28,0.64,1.53,0.33,2.41,2.1,4.51,3.27,2.65,3.2,2.11,0.62,1.19,9.12,1.38,3.12,1.63,0.1,0.14,1.61,0.75,1,1.23,0.44,1.64,1.51,1.3,1.27,2.95,0.63,4.74,0.21,3.56,2.39,0.5,0.37,0.59,0.81,1.01,1.89,1.36,1.51,1.13,1.87,0.69,1.75,null,0.32,2.71,1.84,0.86,0.8,0.81,0.51,0.58,0.95,0.89,0.81,1.38,0.62,0.85,0.93,0.94,1.06,0.87,0.46,1.37,0.78,0.51,0.25,0.29,0.35,0.32,1.08,0.14,0.15,0.26,0.57,0.63,1.26,0.29,0.69,0.58,0.24,0.15,0.37,null,0.21,0.42,0.07,0.12,0.12,0.12,0.21,0.13,0.15,0.12,0.12,0.04,0,null]],"container":"<table class=\"display\">\n  <thead>\n    <tr>\n      <th> <\/th>\n      <th>Country<\/th>\n      <th>Mean<\/th>\n      <th>Median<\/th>\n      <th>SD<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"pageLength":25,"columnDefs":[{"className":"dt-right","targets":[2,3,4]},{"orderable":false,"targets":0}],"order":[],"autoWidth":false,"orderClasses":false,"orderCellsTop":true}},"evals":[],"jsHooks":[]}</script>
</div>

<p> 最后，文中提到用鼠标查看数据是因为本文有一个基于plotly的版本确实可以看到数据，可以到<a href="https://www.whyhow.tk/pages/indiarape.html">这里查看</a>。（友情提示：由于数据内嵌在网页中，这个网页有无情的13MB大）</p>
