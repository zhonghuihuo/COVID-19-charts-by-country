import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
%matplotlib inline

peopledict = {'印度':1352617328,'美国':327167434,'印尼':267663435,'巴基斯坦':212215030,'巴西':209469333,'尼日利亚':195874740,'孟加拉':161356039,'俄罗斯':144478050,'日本':126529100,'墨西哥':126190788,'埃塞俄比亚':109224559,'菲律宾':106651922,'埃及':98423595,'越南':95540395,'刚果（金）':84068091,'德国':82927922,'土耳其':82319724,'伊朗':81800269,'泰国':69428524,'法国':66987244,'英国':66488991,'意大利':60431283,'南非':57779622,'坦桑尼亚':56318348,'缅甸':53708395,'韩国':51635256,'肯尼亚':51393010,'哥伦比亚':49648685,'西班牙':46723749,'乌克兰':44622516,'阿根廷':44494502,'乌干达':42723139,'阿尔及利亚':42228429,'苏丹':41801533,'伊拉克':38433600,'波兰':37978548,'阿富汗':37172386,'加拿大':37058856,'摩洛哥':36029138,'沙特阿拉伯':33699947,'乌兹别克斯坦':32955400,'秘鲁':31989256,'马来西亚':31528585,'安哥拉':30809762,'加纳':29767108,'莫桑比克':29495962,'委内瑞拉':28870195,'也门':28498687,'尼泊尔':28087871,'马达加斯加':26262368,'朝鲜':25549819,'喀麦隆':25216237,'科特迪瓦':25069229,'澳大利亚':24992369,'尼日尔':22442948,'斯里兰卡':21670000,'布基纳法索':19751535,'罗马尼亚':19473936,'马里':19077690,'智利':18729160,'哈萨克斯坦':18276499,'马拉维':18143315,'赞比亚':17351822,'危地马拉':17247807,'荷兰':17231017,'厄瓜多尔':17084357,'叙利亚':16906283,'柬埔寨':16249798,'塞内加尔':15854360,'乍得':15477751,'索马里':15008154,'津巴布韦':14439018,'几内亚':12414318,'卢旺达':12301939,'突尼斯':11565204,'贝宁':11485048,'比利时':11422068,'玻利维亚':11353142,'古巴':11338138,'布隆迪':11175378,'海地':11123176,'南苏丹':10975920,'希腊':10727668,'多米尼加':10627165,'捷克':10625695,'葡萄牙':10281762,'瑞典':10183175,'约旦':9956011,'阿塞拜疆':9942334,'匈牙利':9768785,'阿联酋':9630959,'洪都拉斯':9587522,'白俄罗斯':9485386,'塔吉克斯坦':9100837,'以色列':8883800,'奥地利':8847037,'巴布亚新几内亚':8606316,'瑞士':8516543,'多哥':7889094,'塞拉利昂':7650154,'老挝':7061507,'保加利亚':7024216,'塞尔维亚':6982084,'巴拉圭':6956071,'黎巴嫩':6848925,'利比亚':6678567,'尼加拉瓜':6465513,'萨尔瓦多':6420744,'吉尔吉斯斯坦':6315800,'土库曼斯坦':5850908,'丹麦':5797446,'新加坡':5638676,'芬兰':5518050,'斯洛伐克':5447011,'挪威':5314336,'刚果（布）':5244363,'哥斯达黎加':4999441,'新西兰':4885500,'爱尔兰':4853506,'阿曼':4829483,'利比里亚':4818977,'中非':4666377,'巴勒斯坦':4569087,'毛里塔尼亚':4403319,'巴拿马':4176873,'科威特':4137309,'克罗地亚':4089400,'格鲁吉亚':3731000,'摩尔多瓦':3545883,'乌拉圭':3449299,'波黑':3323929,'波多黎各':3195153,'蒙古':3170208,'亚美尼亚':2951776,'牙买加':2934855,'阿尔巴尼亚':2866376,'立陶宛':2789533,'卡塔尔':2781677,'纳米比亚':2448255,'冈比亚':2280102,'博茨瓦纳':2254126,'加蓬':2119275,'莱索托':2108132,'马其顿':2082958,'斯洛文尼亚':2067372,'拉脱维亚':1926542,'几内亚比绍':1874309,'巴林':1569439,'特立尼达和多巴哥':1389858,'爱沙尼亚':1320884,'赤道几内亚':1308974,'东帝汶':1267972,'毛里求斯':1265303,'塞浦路斯':1189265,'斯威士兰':1136191,'吉布提':958920,'斐济群岛':883483,'科摩罗':832322,'圭亚那':779004,'不丹':754394,'所罗门群岛':652858,'黑山':622345,'卢森堡':607728,'苏里南':575991,'佛得角':543767,'马尔代夫':515696,'马耳他':483530,'文莱':428962,'巴哈马':385640,'伯利兹':383071,'冰岛':353574,'瓦努阿图':292680,'巴巴多斯':286641,'新喀里多尼亚':284060,'法属波利尼西亚':277679,'圣多美和普林西比':211028,'萨摩亚':196130,'圣卢西亚':181889,'关岛':165768,'库拉索':159849,'基里巴斯':115847,'密克罗尼西亚联邦':112640,'格林纳达':111454,'圣文森特和格林纳丁斯':110210,'阿鲁巴':105845,'汤加':103197,'塞舌尔':96762,'安提瓜和巴布达':96286,'马恩岛':84077,'安道尔':77006,'多米尼克':71625,'开曼群岛':64174,'百慕大':63968,'马绍尔群岛':58413,'北马里亚纳群岛':56882,'格陵兰':56025,'美属萨摩亚':55465,'圣基茨和尼维斯':52441,'法罗群岛':48497,'荷属圣马丁':40654,'摩纳哥':38682,'列支敦士登':37910,'特克斯和凯科斯群岛':37665,'法属圣马丁':37264,'圣马力诺':33785,'直布罗陀':33718,'英属维尔京群岛':29802,'帕劳':17907,'瑙鲁':12704,'图瓦卢':11508,'厄立特里亚':6700000,'梵蒂冈':800,'纽埃':1620}

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
        if rankitem['name'] in peopledict:
            rankdict[rankitem['name']] = rankitem['confirm'] * 10000000 // peopledict[rankitem['name']]
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
        plt.title('新冠累计确诊人口比例', fontproperties=myfont, fontsize=16)
        plt.xlim((0, len(x)))
        plt.xticks(np.linspace(0, len(x), len(x) + 1))
        ax.set_xticklabels(x, rotation=0, fontsize='small')
        plt.xlabel('日期', fontproperties=myfont, fontsize=16)
        plt.ylabel('比例（千万分比）', fontproperties=myfont, fontsize=16)
        plt.grid(True)
        flag = True

    f = open('data/' + rankitem[0] + '.json', 'r', encoding='utf-8')
    datalist = json.loads(f.read())
    f.close()

    y = []
    confirmdict = {}
    for dataitem in datalist['data']:
        if dataitem['date'].replace('.', '') not in confirmdict:
            confirmdict[dataitem['date'].replace('.', '')] = dataitem['confirm'] * 10000000 // peopledict[rankitem[0]]
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
        plt.savefig('./test03.' + str(i // 8) + '.png')
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
    plt.savefig('./test03.' + str((i + 7) // 8) + '.png')
