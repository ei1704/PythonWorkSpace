import os

path = 'files/word.txt'

if os.path.exists(path):
    with open(path, 'r') as f:
        cnt = 1
        for line in f:
            temp = line.strip()
            print('{:04}:{}'.format(cnt, temp))
            cnt += 1
