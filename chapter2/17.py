f = open('./chapter2/col1.txt')
s = f.read()
f.close()

print(set(s.split()))
