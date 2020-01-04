f = open('./chapter2/col1.txt')
s1 = f.read()
f.close()

f = open('./chapter2/col2.txt')
s2 = f.read()
f.close()

ans = ""

for i in range(24):
    ans += s1.split()[i] + "   " + s2.split()[i] + "\n"


f = open('./chapter2/merge.txt', mode='w')
f.write(ans)
f.close()
