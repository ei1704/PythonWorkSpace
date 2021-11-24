import os
import re

word_list = {}

if os.path.exists('files/sentence.txt'):
    with open('files/sentence.txt', 'r') as f:
        for line in f:
            temp = re.split('[^\w(?!\')]', line)
            # print(temp)
            for i in temp:
                # m = re.search('[A-Za-z\']+', i)
                # word = m.group().lower()
                word = i.lower()
                if '(' in word:
                    word = word[1:len(word)-1]

                if word in word_list:
                    word_list[word] += 1
                else:
                    word_list[word] = 1

        word_list = sorted(word_list.items())
        for i in word_list:
            key, val = i
            if key == '':
                continue
            print("{:15s}:{}".format(key, val))
