import sys

args = sys.argv

n = args[1]

f = open('./chapter2/hightemp.txt')
s = f.read()
f.close()

arr = s.split('\n')

for i in range(int(n)):
    print(arr[i])
