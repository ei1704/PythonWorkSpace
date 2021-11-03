import os

word_list = []

if os.path.exists('files/word.txt'):
    with open('files/word.txt', 'r') as f:
        for line in f:
            # print(line.strip())
            word_list.append(line.strip())

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


with open('files/word.txt', 'w', encoding='utf-8', newline='\n') as f:
    for i in word_list:
        f.write(i+"\n")
