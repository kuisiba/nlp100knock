f = open('./chapter2/hightemp.txt')
s = f.read()
f.close()

s = s.split('\n')

arr = []
for i in s:
    arr.append(i.split())
arr.pop()

#ss = sorted(arr, key=lambda x:float(x[2]))
arr.sort(key=lambda x: x[2], reverse=True)

for i in arr:
    print(i)
