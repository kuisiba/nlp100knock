import collections

f = open('./chapter2/hightemp.txt')
s = f.read()
f.close()

s = s.split('\n')
s.pop()
arr = []
for i in s:
    t = i.split()[0]
    arr.append(t)

ss = collections.Counter(arr)
print(ss)
