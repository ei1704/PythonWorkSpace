import os

if os.path.exists('files/test.csv'):
    with open('files/test.csv', 'r', encoding="utf-8") as f:
        cnt = 0
        for line in f:
            if cnt == 0:
                cnt += 1
                continue
            name, ja, ma, si, so = line.strip().split(",")
            print(f'{name} {int(ja)+int(ma)+int(si)+int(so)}')
