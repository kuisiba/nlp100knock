f = open('./chapter2/hightemp.txt')
s = f.read()
f.close()

print(s.replace('\t', ' '))
