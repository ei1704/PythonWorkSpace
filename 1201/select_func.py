# 関数を辞書で渡し、実行する
def func1():
    print("Hello")


def func2():
    print("Goodbye")


# main
run_list = {'a': func1, 'b': func2}

while True:
    c = input("a=>Hello,b=>Goodbye\nどちらを実行しますか？: ")
    if c == "":
        break
    elif c != 'a' and c != 'b':
        print("どちらかを選択してください。")
        continue
    run_list[c]()
