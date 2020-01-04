def f(i, s):
    if i == 1 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 15 or i == 16 or i == 19:
        return s[0]
    else:
        return s[0:2]


s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

arr = s.split()

dict = {}
for i, x in enumerate(arr):
    dict[f(i + 1, x)] = i + 1

print(dict)
