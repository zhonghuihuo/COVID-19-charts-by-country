import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#import matplotlib.colors as colors
%matplotlib inline

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
        rankdict[rankitem['name']] = rankitem['confirmAdd']
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
        plt.title('新冠新增确诊', fontproperties=myfont, fontsize=16)
        plt.xlim((0, len(x)))
        plt.xticks(np.linspace(0, len(x), len(x) + 1))
        ax.set_xticklabels(x, rotation=0, fontsize='small')
        plt.xlabel('日期', fontproperties=myfont, fontsize=16)
        plt.ylabel('数量', fontproperties=myfont, fontsize=16)
        plt.grid(True)
        flag = True

    f = open('data/' + rankitem[0] + '.json', 'r', encoding='utf-8')
    datalist = json.loads(f.read())
    f.close()

    y = []
    confirmdict = {}
    for dataitem in datalist['data']:
        if dataitem['date'].replace('.', '') not in confirmdict:
            confirmdict[dataitem['date'].replace('.', '')] = dataitem['confirm_add']
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
        plt.savefig('./test02.' + str(i // 8) + '.png')
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
    plt.savefig('./test06.' + str((i + 7) // 8) + '.png')
