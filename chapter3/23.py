import re

f = open('chapter3/igirisu.txt')
lines = f.readlines()
f.close()

for line in lines:
    if re.search(r'={2,}', line):
        print(line)
        counter = 0
        for c in line:
            if c == '=':
                counter += 1
            else:
                break
        print(counter - 1)
