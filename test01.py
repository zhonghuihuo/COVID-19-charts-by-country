import requests
import json

#请找合适数据源抓取
url = 'https://...'
req = requests.get(url)
f = open('data/ranklist.json', 'w', encoding='utf-8')
f.write(bytes.decode(req.content))
f.close()

ranklist = json.loads(req.content)

for rankitem in ranklist['data']:
    print(rankitem['name'])
    #请找合适数据源抓取
    url = 'https://...?country=' + rankitem['name']
    req = requests.get(url)
    
    f = open('data/' + rankitem['name'] + '.json', 'w', encoding='utf-8')
    f.write(bytes.decode(req.content))
    f.close()
print("OK!")
