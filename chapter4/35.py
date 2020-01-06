import MeCab
import re

mecab = MeCab.Tagger('-MeCab')

f = open('./chapter4/neko.txt.mecab')
neko = f.readlines()
f.close()

arr = []
meisi_arr = []
t = ""
for i in range(len(neko)):
    matched = re.match(
        r'(.*)\t(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)',
        neko[i])
    sentence = {}
    if matched:
        sentence['surface'] = matched.group(1)
        sentence['base'] = matched.group(8)
        sentence['pos'] = matched.group(2)
        sentence['pos1'] = matched.group(3)
    if '名詞' in sentence.values():
        arr.append(sentence['surface'])
    else:
        if len(arr) == 0 or len(arr) == 1:
            arr.clear()
            continue
        t = ''
        for meisi in arr:
            t += meisi
        meisi_arr.append(t)
        arr.clear()


for i in meisi_arr:
    print(i)
