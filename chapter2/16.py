import sys

args = sys.argv
n = args[1]
n = int(n)

f = open('./chapter2/hightemp.txt')
s = f.read()
f.close()

arr = s.split('\n')
arr.pop()

ooi = len(arr) % n
ooi_line = len(arr) // n + 1
sukunai = n - ooi
sukunai_line = len(arr) // n

splitted = ["" for i in range(ooi + sukunai)]

ooi_all_line = ooi * ooi_line
offset = int(ooi_all_line / ooi_line)

for i in range(len(arr)):
    if i < ooi_all_line:
        splitted[i // ooi_line] += arr[i]
        splitted[i // ooi_line] += '\n'
    else:
        splitted[offset + (i - ooi_all_line) // sukunai_line] += arr[i]
        splitted[offset + (i - ooi_all_line) // sukunai_line] += '\n'

for i in range(len(splitted)):
    path = './chapter2/' + str(i)
    print(path)
    f = open(path, mode='w')
    f.write(splitted[i])
    f.close()
