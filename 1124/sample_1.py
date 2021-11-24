while True:
    num = int(input("整数を入力してください(終了->0):"))
    if num == 0:
        break
    else:
        print("偶数" if num % 2 == 0 else "奇数")
