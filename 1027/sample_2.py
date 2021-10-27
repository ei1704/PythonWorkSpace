fruits = ['バナナ', 'リンゴ', 'オレンジ']
while True:
    n = input("果物をカタカナで入力してください:")
    if n == "":
        break
    elif n in fruits:
        print("{}は、知っています！".format(n))
    else:
        print("{}は、知りませんでした。覚えておきます。".format(n))
        fruits.append(n)

print('知っている果物')
print(fruits)
