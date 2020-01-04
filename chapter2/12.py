f = open('./chapter2/hightemp.txt')
s = f.read()
f.close()

col1 = []
col2 = []
for i, x in enumerate(s.split()):
    if i % 4 == 0:
        col1.append(x)
    elif i % 4 == 1:
        col2.append(x)

f = open('./chapter2/col1.txt', mode='w')
f.write('\n'.join(col1))
f.close()

f = open('./chapter2/col2.txt', mode='w')
f.write('\n'.join(col2))
f.close()
