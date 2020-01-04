f = open('./chapter2/hightemp.txt')
s = f.read()
print(s)
f.close()

print(s.count('\n'))
