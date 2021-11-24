def tax_included(val, tax=10):
    num = "None"
    if val > 0 and tax > 0:
        num = val + val * (tax/100)
        num = int(num)
    if tax == 10:
        ret = "{}の税込み金額は{}円".format(val, num)
    else:
        ret = "{}の消費税{}%の税込み金額は{}円".format(val, tax, num)
    return ret


print(tax_included(5000))
print(tax_included(5000, 8))
print(tax_included(5000, -5))
