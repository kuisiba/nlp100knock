import re

f = open('chapter3/igirisu.txt')
lines = f.readlines()
f.close()

for line in lines:
    res = re.match(r'^\[\[Category:(.*?)(\|\*)?\]\].*$', line)
    if res is not None:
        print(res.group(1))
