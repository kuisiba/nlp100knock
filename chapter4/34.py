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
    if 'の' in sentence.values() and '連体化' in sentence.values():
        mae_matched = re.match(
            r'(.*)\t(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)', neko[i - 1])
        ushiro_matched = re.match(
            r'(.*)\t(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)', neko[i + 1])
        if mae_matched and ushiro_matched:
            s = mae_matched.group(
                1) + sentence['surface'] + ushiro_matched.group(1)
            arr.append(s)

for i in arr:
    print(i)
