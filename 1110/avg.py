import os

if os.path.exists('files/test.csv'):
    with open('files/test.csv', 'r', encoding="utf-8") as f:
        cnt = 0
        sub = f.readline().strip().split(",")
        sub = sub[1:]
        print(sub)
        sums = [0 for i in range(len(sub))]
        for line in f:
            temp = line.strip().split(",")
            temp = temp[1:]
            for i in range(len(temp)):
                sums[i] += int(temp[i])
            cnt += 1
            avgs = []
        for i in sums:
            avgs.append(i/cnt)
        print(avgs)
