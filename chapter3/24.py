import re

f = open('chapter3/igirisu.txt')
lines = f.readlines()
f.close()

for line in lines:
    ret = re.match(r'^\[\[(File|ファイル):(.*)(\|thumb)(.*$)', line)
    if ret:
        print(ret.group(2))
