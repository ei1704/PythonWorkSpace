import os
import pickle

word_list = []

if os.path.exists('files/word.pkl'):
    with open('files/word.pkl', 'rb') as f:
        word_list = pickle.load(f)

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


with open('files/word.pkl', 'wb') as f:
    pickle.dump(word_list, f)
