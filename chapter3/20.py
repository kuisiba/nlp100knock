import json
import gzip

f = gzip.open('./chapter3/jawiki-country.json.gz', mode='rt')
for l in f:
    data = json.loads(l)
    if data['title'] == 'イギリス':
        data['text'] = data['text'].replace('\n', '')
        fw = open('./chapter3/igirisu.json', 'w')
        json.dump(data, fw, ensure_ascii=False)
