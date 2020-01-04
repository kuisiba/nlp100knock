def ngram(s, n):
    arr = []
    for i in range(len(s) - n + 1):
        arr.append(s[i:i + n])
    return arr


s1 = "paraparaparadise"
s2 = "paragraph"

X = ngram(s1, 2)
Y = ngram(s2, 2)

print(set(X) | set(Y))
print(set(X) & set(Y))
print(set(X) - set(Y))
