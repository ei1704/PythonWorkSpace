a = int(input("数字１："))
b = int(input("数字２："))

# 入れ替え
if a > b:
    a, b = b, a

l = range(a, b+1)
print("{}から{}までの合計は{}です".format(a, b, sum(l)))
