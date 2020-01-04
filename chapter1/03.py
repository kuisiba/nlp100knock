import re

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

ss = re.sub(r'[,.]', '', s)
sss = map(lambda x: len(x), ss.split())
ans = ""
for i in sss:
    ans += str(i)

print(ans)
