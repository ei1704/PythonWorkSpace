import os
import re

word_list = {}

if os.path.exists('files/sentence.txt'):
    with open('files/sentence.txt', 'r') as f:
        for line in f:
            temp = re.split('[^\w?!\']', line)
            # print(temp)
            for i in temp:
                if i == "":
                    continue
                word = i.lower()
                if word in word_list:
                    word_list[word] += 1
                else:
                    word_list[word] = 1

        word_list = sorted(word_list.items())
        for i in word_list:
            key, val = i
            print("{:15s}:{}".format(key, val))
