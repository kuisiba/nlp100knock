def ngram(s, n):
    arr = []
    for i in range(len(s) - n + 1):
        arr.append(s[i:i + n])
    return arr


s = "I am an NLPer"

words = s.split()
print(ngram(words, 2))

chars = list(s)
print(ngram(chars, 2))
