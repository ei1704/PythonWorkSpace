import os

if os.path.exists('files/word.txt'):
    with open('files/word.txt', 'r') as f:
        cnt = 1
        for line in f:
            temp = line.strip()
            print('{:04}:{}'.format(cnt, temp))
            cnt += 1
