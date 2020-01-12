import re

f = open('./chapter6/nlp.txt.xml')
s = f.read()
f.close()

pattern = re.compile(r'<word>(.*?)</word>')

matched = pattern.findall(s)

for i in matched:
    print(i)
