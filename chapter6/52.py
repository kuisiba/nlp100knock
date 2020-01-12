import re
import nltk

f = open('chapter6/nlp.txt')
lines = f.readlines()
f.close()

pattern = re.compile(r'(^.*?[\.|;|:|\?|\!])\s([A-Z].*)')

arr = []
for x in lines:
    x = x.strip()
    while len(x) > 0:
        matched = pattern.match(x)
        if matched:
            arr.append(matched.group(1))
            x = matched.group(2)
        else:
            arr.append(x)
            x = ''

arr2 = []
for element in arr:
    element = element.split(' ')
    for element2 in element:
        arr2.append(element2)
    arr2.append("")

stemmer = nltk.stem.porter.PorterStemmer()

for i, x in enumerate(arr2):
    x = x.replace('.', '')
    t = x
    t += "  "
    t += stemmer.stem(x)
    print(t)
