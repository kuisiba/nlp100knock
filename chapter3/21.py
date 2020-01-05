f = open('chapter3/igirisu.txt')
lines = f.readlines()
f.close()

for line in lines:
    if 'Category' in line:
        print(line)
