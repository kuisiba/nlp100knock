import json
import gzip

f = gzip.open('./chapter3/jawiki-country.json.gz', mode='rt')
for l in f:
    data = json.loads(l)
    if data['title'] == 'イギリス':
        print(data['text'])
        fw = open('./chapter3/igirisu.txt', 'w')
        fw.write(data['text'])
        fw.close()
