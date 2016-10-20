# 亵渎补奸计划

10.18
---

想做点什么，想了一晚上，把我最喜欢的小说《亵渎》弄一下吧，就叫它"亵渎补奸计划"。<br />

1.使用python模块jieba做分词<br />
2.词频统计<br />
3.得到小说中出现概率最高的几个词<br />
4.搭配另一个模块WorldCloud，作词云标签<br />
5.载入一张图片，把它做成二维数组，载入词云<br />
6.以××照片为词云背景<br />

10.19
---

把第一章跑了一下：

WordCount 统计词频，打印到文本中
![enter image description here](http://oa4pac8sx.bkt.clouddn.com/2016-10-19%2021:25:38%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
WordCloudSquere 输出词云
![enter image description here](http://oa4pac8sx.bkt.clouddn.com/Squere.jpg)
WordCloudPlot 以图片位模板输出
![enter image description here](http://oa4pac8sx.bkt.clouddn.com/Mask.jpg)

10.20
---
但是仅仅这样存在一些问题，很多没有用的词占了很大部分：
![enter image description here](http://oa4pac8sx.bkt.clouddn.com/2016-10-20%2010:11:02%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
所以词性做一下筛选，使用jieba.posseg，第一次去掉很多词性，发现还是有很多不科学的东东，然后保留名词动词，会，说。。。很多也应该去掉，最后干脆只保留名词，效果还不错。
![enter image description here](http://oa4pac8sx.bkt.clouddn.com/2016-10-20%2010:13:48%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
![enter image description here](http://oa4pac8sx.bkt.clouddn.com/Squere2.jpg)
![enter image description here](http://oa4pac8sx.bkt.clouddn.com/Mask2.jpg)

