import os

word_list = {}

if os.path.exists('files/word_list.txt'):
    with open('files/word_list.txt', 'r') as f:
        for line in f:
            # print(line.strip())
            word = line.strip()
            if word in word_list:
                word_list[word] += 1
            else:
                word_list[word] = 1

        word_list = sorted(word_list.items())
        for i in word_list:
            key, val = i
            print("{}:{}".format(key, val))
