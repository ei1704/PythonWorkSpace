def tax_included(val, tax=10):
    '''税込み金額を計算する。税率を省略した場合は10%になる'''
    num = "None"
    if val > 0 and tax > 0:
        num = val + val * (tax/100)
    return num


print("{}の税込み金額は{}円".format(5000, tax_included(5000)))
print("{}の消費税{} % の税込み金額は{}円".format(5000, 8, tax_included(5000, 8)))
print("{}の消費税{} % の税込み金額は{}円".format(5000, -5, tax_included(5000, -5)))
