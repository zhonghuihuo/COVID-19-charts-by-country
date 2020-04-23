# 2019新型冠状病毒（COVID-19/2019-nCoV）全球各国疫情状况图表对比分析

本项目为2019新型冠状病毒（COVID-19/2019-nCoV）全球各国疫情状况的图表对比分析而创建，包括采集数据、累计确诊对比、累计确诊人口比例对比、累计确诊面积对比、累计确诊人口密度对比、新增确诊对比。疫情数据、各国人口数据、各国面积数据均来自网络，仅供学习参考。

# 数据说明
各国人口数据：python代码内json数据（人）

各国面积数据：python代码内json数据（平方公里）

各国疫情数据：每天采集新数据，包括累计确诊数、每日新增确诊数等（人）

# 程序说明

## test01.py
采集当日最新数据，保存为json文件供其他程序读取使用

## test02.py
读取json文件疫情数据，按各国累计确诊数排序生成多张图表（为图表对比更加明显，采用8个国家一张图表）
由图表可直观了解各国累计病例的变化趋势及与其他国家的对比情况。

![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test02.1.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test02.2.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test02.3.png)

## test03.py
读取json文件疫情数据，按各国累计确诊数与本国总人口比例排序生成多张图表（为图表对比更加明显，采用8个国家一张图表）
由图表可直观了解各国累计病例与本国总人口比例的变化趋势及与其他国家的对比情况。

同样的确诊人数，对于人口越少的国家，此图表比例越高。

![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test03.1.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test03.2.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test03.3.png)

## test04.py
读取json文件疫情数据，按各国累计确诊数与本国面积比例排序生成多张图表（为图表对比更加明显，采用8个国家一张图表）
由图表可直观了解各国累计病例与本国面积比例的变化趋势及与其他国家的对比情况。

同样的确诊人数，对于国土面积越少的国家，此图表比例越高。

![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test04.1.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test04.2.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test04.3.png)

## test05.py
读取json文件疫情数据，按各国累计确诊数与本国人口密度比例排序生成多张图表（为图表对比更加明显，采用8个国家一张图表）
由图表可直观了解各国累计病例与本国人口密度比例的变化趋势及与其他国家的对比情况。

同样的确诊人数，对于人口密度越小的国家，此图表比例越高。

![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test05.1.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test05.2.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test05.3.png)

## test06.py
读取json文件疫情数据，按新增确诊数排序生成多张图表（为图表对比更加明显，采用8个国家一张图表）
由图表可直观了解各国新增病例的变化趋势及与其他国家的对比情况。

![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test06.1.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test06.2.png)
![img](https://raw.githubusercontent.com/zhonghuihuo/COVID-19-charts-by-country/master/test06.3.png)

# 疫情汹汹，时不我待。各国当迅速携起手来，聚全球合力遏制疫情蔓延，不容有任何懈怠与麻痹大意。

