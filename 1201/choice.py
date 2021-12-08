def odd():
    print("奇数")


def even():
    print("偶数")


def choice_func(number):
    return even if int(number) % 2 == 0 else odd


# main
while True:
    num = input("数字を入力してください。（0：終了）")
    if num == "0":
        break
    elif not num.isdecimal():
        print("入力が正しくありません")
        continue
    choice_func(num)()
