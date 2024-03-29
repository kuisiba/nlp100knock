import re


def f(kiso):
    flag = False
    kakko_flag = False
    tmp = ""
    ret = []
    for i in kiso:
        if i == '|':
            if flag == False:
                flag = True
            else:
                if kakko_flag == False:
                    ret.append(tmp)
                    tmp = ''
        if i != '|':
            if i == '{' or i == '[':
                kakko_flag = True
            elif i == '}' or i == ']':
                kakko_flag = False
            if flag == True:
                if i != '\'':
                    tmp += i
    return ret


def g(kiso_list):
    ret = {}
    for i in kiso_list:
        matched = re.match(r'(^.*)\s=\s(.*$)', i)
        ret[matched.group(1)] = matched.group(2)
    return ret


fr = open('chapter3/igirisu.txt')
s = fr.read()
fr.close()

kiso = re.findall(r'基礎情報(.*)(^\}\}$)', s, flags=(re.DOTALL | re.MULTILINE))
kiso = kiso[0][0].replace('\n', '')
kiso_list = f(kiso)
kiso_dic = g(kiso_list)
for k, v in kiso_dic.items():
    print(k, v)
