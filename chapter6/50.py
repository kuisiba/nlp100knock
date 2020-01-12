import re

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

for element in arr:
    print(element)
