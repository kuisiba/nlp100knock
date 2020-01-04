def cipher(s):
    arr = list(s)
    ans = []
    for i in arr:
        if i.islower():
            ans.append(chr(219 - ord(i)))
        else:
            ans.append(i)
    print(ans)


cipher("abcxyzABCXYZ")
