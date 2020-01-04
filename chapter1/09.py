import random


def conv(s):
    if len(s) <= 4:
        return s
    else:
        begin = s[0]
        end = s[-1]
        ss = list(s[1:-1])
        sss = random.sample(ss, len(ss))
        ret = begin + "".join(sss) + end
        return ret


s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

ans = ""

for i in s.split():
    ans += conv(i) + " "

print(ans)
