def out_csvdata(**kwargs):
    li = []
    k = ['B', 'L', 'D']
    for i in k:
        if i in kwargs:
            li.append(kwargs[i])
        else:
            li.append("-")
    print(li)


# main
eat = {}
while True:
    menu = input("朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：")
    if menu == '':
        break
    token, menu = menu.split(',')
    if token in ['B', 'L', 'D']:
        eat[token] = menu
    else:
        print('記号が間違っています。登録しません')
        continue
out_csvdata(**eat)
