def list2int(s):
    """文字列を数値に変換した値を返す"""
    if type(s) is list:
        li = []
        for i in s:
            if type(i) is int:
                li.append(i)
            elif type(i) is not str:
                li.append("0")
            elif i.isalpha():
                li.append("0")
            elif i.isdecimal():
                li.append(int(i))
        return li
    elif s.isalpha():
        return "0"
    elif s.isdecimal():
        return int(s)
    else:
        return "None"


print(list2int(['5', 'ab', '100', 10, 1]))
print(list2int('100'))
print(list2int('xyz'))
