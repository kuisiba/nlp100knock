import MeCab
import re

mecab = MeCab.Tagger('-MeCab')

f = open('./chapter4/neko.txt.mecab')
neko = f.readlines()
f.close()

arr = []
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
    if 'サ変接続' in sentence.values():
        arr.append(sentence)

for i in arr:
    print(i)
