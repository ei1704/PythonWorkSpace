def check_shopping(**kwargs):
    flg = True
    for k, v in kwargs.items():
        if v < 100:
            flg = False
            break

    return flg


def check_shopping2(**kwargs):
    min_price = min(kwargs.values())
    if min_price < 100:
        return False
    else:
        return True


    # main
dic_order = {}
while True:
    product_name = input('商品名を入力してください（0:終了）：')
    if product_name == '0':
        break
    product_price = input('金額を入力してください（0:終了）：')
    if product_price == '0':
        break
    elif product_price.isnumeric():
        product_price = int(product_price)
    else:
        print("数値以外が入力されました")
        continue
    dic_order[product_name] = product_price
if check_shopping2(**dic_order):
    print('\n全てのデータは問題ありませんでした')
else:
    print('\n最低価格を下回った商品があります。')
for key, value in dic_order.items():
    print(f'{key} : {value}')
