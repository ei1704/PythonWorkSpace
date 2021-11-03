word_list = []
while True:
    word = input("単語を入力してください：")
    if word == "":
        print("終了します")
        break
    elif word == "LIST":
        print(f'単語リスト：{word_list}')
    elif word in word_list:
        print("既に登録済みです")
    else:
        word_list.append(word)

print(f'これまでに覚えた単語：{word_list}')
