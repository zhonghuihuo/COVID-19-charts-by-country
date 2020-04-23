import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
%matplotlib inline

areadict = {'俄罗斯':17098250,'加拿大':9984670,'美国':9831510,'巴西':8515770,'澳大利亚':7741220,'印度':3287259,'阿根廷':2780400,'哈萨克斯坦':2724901,'阿尔及利亚':2381740,'刚果（金）':2344860,'沙特阿拉伯':2149690,'墨西哥':1964375,'印尼':1913580,'苏丹':1879357,'利比亚':1759540,'伊朗':1745150,'蒙古':1564120,'秘鲁':1285220,'乍得':1284000,'尼日尔':1267000,'安哥拉':1246700,'马里':1240190,'南非':1219090,'哥伦比亚':1141748,'埃塞俄比亚':1104300,'玻利维亚':1098580,'毛里塔尼亚':1030700,'埃及':1001450,'坦桑尼亚':947300,'尼日利亚':923770,'委内瑞拉':912050,'纳米比亚':824290,'巴基斯坦':796100,'莫桑比克':786380,'土耳其':785350,'智利':756700,'赞比亚':752610,'缅甸':676590,'阿富汗':652860,'南苏丹':644330,'索马里':637660,'挪威':625217,'中非':622980,'乌克兰':603550,'马达加斯加':587295,'博茨瓦纳':581730,'肯尼亚':580370,'法国':549086,'也门':527970,'泰国':513120,'西班牙':505935,'土库曼斯坦':488100,'喀麦隆':475440,'巴布亚新几内亚':462840,'瑞典':447430,'乌兹别克斯坦':447400,'摩洛哥':446550,'伊拉克':435051,'格陵兰':410450,'巴拉圭':406751,'津巴布韦':390760,'日本':377970,'德国':357580,'刚果（布）':342000,'芬兰':338450,'越南':331230,'马来西亚':330345,'科特迪瓦':322460,'波兰':312680,'阿曼':309500,'意大利':301340,'菲律宾':300000,'布基纳法索':274220,'新西兰':267710,'加蓬':267670,'厄瓜多尔':256370,'几内亚':245860,'英国':243610,'乌干达':241550,'加纳':238540,'罗马尼亚':238400,'老挝':236800,'圭亚那':214970,'白俄罗斯':207600,'吉尔吉斯斯坦':199950,'塞内加尔':196710,'叙利亚':185180,'柬埔寨':181040,'乌拉圭':176220,'苏里南':163820,'突尼斯':163610,'孟加拉':147630,'尼泊尔':147180,'塔吉克斯坦':141380,'希腊':131960,'尼加拉瓜':130370,'朝鲜':120540,'马拉维':118480,'厄立特里亚':117600,'贝宁':114760,'洪都拉斯':112490,'利比里亚':111370,'保加利亚':111000,'古巴':109880,'危地马拉':108890,'冰岛':103000,'韩国':100339,'匈牙利':93030,'葡萄牙':92225,'约旦':89320,'塞尔维亚':88360,'阿塞拜疆':86600,'奥地利':83879,'阿联酋':83600,'捷克':78870,'巴拿马':75420,'塞拉利昂':72300,'爱尔兰':70280,'格鲁吉亚':69700,'斯里兰卡':65610,'立陶宛':65286,'拉脱维亚':64490,'多哥':56790,'克罗地亚':56590,'波黑':51210,'哥斯达黎加':51100,'斯洛伐克':49030,'多米尼加':48670,'爱沙尼亚':45340,'丹麦':42920,'荷兰':41540,'瑞士':41290,'不丹':38393,'几内亚比绍':36130,'摩尔多瓦':33850,'比利时':30530,'莱索托':30360,'亚美尼亚':29740,'所罗门群岛':28900,'阿尔巴尼亚':28750,'赤道几内亚':28050,'布隆迪':27830,'海地':27750,'卢旺达':26340,'马其顿':25710,'吉布提':23200,'伯利兹':22970,'以色列':22070,'萨尔瓦多':21040,'斯洛文尼亚':20675,'新喀里多尼亚':18580,'斐济群岛':18270,'科威特':17820,'斯威士兰':17360,'东帝汶':14870,'巴哈马':13880,'黑山':13810,'瓦努阿图':12190,'卡塔尔':11610,'冈比亚':11300,'牙买加':10990,'黎巴嫩':10450,'塞浦路斯':9250,'波多黎各':8870,'巴勒斯坦':6020,'文莱':5770,'特立尼达和多巴哥':5130,'百慕大':4290,'佛得角':4030,'法属波利尼西亚':4000,'萨摩亚':2840,'卢森堡':2590,'毛里求斯':2040,'科摩罗':1861,'法罗群岛':1396,'圣多美和普林西比':960,'特克斯和凯科斯群岛':950,'基里巴斯':810,'巴林':778,'多米尼克':750,'汤加':750,'新加坡':719,'密克罗尼西亚联邦':700,'圣卢西亚':620,'马恩岛':570,'关岛':540,'安道尔':470,'塞舌尔':460,'北马里亚纳群岛':460,'帕劳':460,'库拉索':444,'安提瓜和巴布达':440,'巴巴多斯':430,'圣文森特和格林纳丁斯':390,'格林纳达':340,'马耳他':320,'马尔代夫':300,'圣基茨和尼维斯':260,'开曼群岛':260,'美属萨摩亚':200,'马绍尔群岛':180,'阿鲁巴':180,'列支敦士登':160,'英属维尔京群岛':150,'圣马力诺':60,'法属圣马丁':54,'荷属圣马丁':34,'图瓦卢':30,'瑙鲁':20,'直布罗陀':10,'摩纳哥':2}

f = open('data/ranklist.json', 'r', encoding='utf-8')
ranklist = json.loads(f.read())
f.close()
#print(ranklist)

dateset = set(())
for rankitem in ranklist['data']:
    f = open('data/' + rankitem['name'] + '.json', 'r', encoding='utf-8')
    datalist = json.loads(f.read())
    f.close()
    for dataitem in datalist['data']:
        if dataitem['date'].replace('.', '') not in dateset:
            dateset.add(dataitem['date'].replace('.', ''))
#print(dateset)
datelist = list(dateset)
#print(datelist)
datelist.sort()
#print(datelist)

x = []
for i in range(0, len(datelist)):
    if i % 3 != 0:
        x.append('')
    else:
        x.append(datelist[i])

rankdict = {}
for rankitem in ranklist['data']:
    if rankitem['name'] not in rankdict:
        if rankitem['name'] in areadict:
            rankdict[rankitem['name']] = rankitem['confirm'] * 100000 // areadict[rankitem['name']]
#print(rankdict)
rankdict = sorted(rankdict.items(), key=lambda asd:asd[1], reverse=True)
#print(rankdict)

myfont = fm.FontProperties(fname='kaiti.ttf')
myColor = ['#000000', '#FF0000', '#00FF00', '#0000FF', '#00FFFF', '#FF00FF', '#FFFF00', '#808080']

i = 0
flag = False
ylimit = 0
for rankitem in rankdict:
    print(rankitem[0])
    if i % 8 == 0:
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111)
        plt.title('新冠累计确诊人口面积比例', fontproperties=myfont, fontsize=16)
        plt.xlim((0, len(x)))
        plt.xticks(np.linspace(0, len(x), len(x) + 1))
        ax.set_xticklabels(x, rotation=0, fontsize='small')
        plt.xlabel('日期', fontproperties=myfont, fontsize=16)
        plt.ylabel('比例（平方公里十万分比）', fontproperties=myfont, fontsize=16)
        plt.grid(True)
        flag = True

    f = open('data/' + rankitem[0] + '.json', 'r', encoding='utf-8')
    datalist = json.loads(f.read())
    f.close()

    y = []
    confirmdict = {}
    for dataitem in datalist['data']:
        if dataitem['date'].replace('.', '') not in confirmdict:
            confirmdict[dataitem['date'].replace('.', '')] = dataitem['confirm'] * 100000 // areadict[rankitem[0]]
    #print(confirmdict)
    
    lastconfirm = 0
    for dateitem in datelist:
        if dateitem in confirmdict:
            y.append(confirmdict[dateitem])
            lastconfirm = confirmdict[dateitem]
            if confirmdict[dateitem] > ylimit:
                ylimit = confirmdict[dateitem]
        else:
            y.append(lastconfirm)
    
    plt.plot(datelist, y, color=myColor[i % 8], marker='o', linestyle='-', label=rankitem[0])
    i = i + 1

    if i % 8 == 0:
        if ylimit > 999999:
            ylimit = (ylimit + 9999) // 10000 * 10000
        elif ylimit > 9999:
            ylimit = (ylimit + 999) // 1000 * 1000
        elif ylimit > 99:
            ylimit = (ylimit + 99) // 100 * 100
        else:
            ylimit = (ylimit + 9) // 10 * 10
        plt.ylim((0, ylimit))
        plt.yticks(np.linspace(0, ylimit, 11))
        plt.legend(prop=myfont, loc='upper left')
        leg = plt.gca().get_legend()
        ltext = leg.get_texts()
        plt.setp(ltext, fontsize='16')
        plt.savefig('./test04.' + str(i // 8) + '.png')
        ylimit = 0
        flag = False

if flag == True:
    if ylimit > 999999:
        ylimit = (ylimit + 9999) // 10000 * 10000
    elif ylimit > 9999:
        ylimit = (ylimit + 999) // 1000 * 1000
    elif ylimit > 99:
        ylimit = (ylimit + 99) // 100 * 100
    else:
        ylimit = (ylimit + 9) // 10 * 10
    plt.ylim((0, ylimit))
    plt.yticks(np.linspace(0, ylimit, 11))
    plt.legend(prop=myfont, loc='upper left')
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize='16')
    plt.savefig('./test04.' + str((i + 7) // 8) + '.png')
