def str2int(s):
    """文字列を数値に変換した値を返す"""
    if type(s) is int:
        return s
    elif s.isdecimal():
        return int(s)
    else:
        return 0

print(str2int('a'))
print(str2int('10'))
print(str2int(100))
