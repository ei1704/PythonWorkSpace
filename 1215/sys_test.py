import os
import sys

argv = sys.argv

if len(argv) == 1:
  print("引数なし")
else:

  print(f"引数：{argv}")

  for i in argv[1:]:
    print(f"---{i}---")
    path = '../files/'+i

    if os.path.exists(path):
      with open(path, 'r') as f:
        cnt = 1
        for line in f:
            temp = line.strip()
            print('{:04}:{}'.format(cnt, temp))
            cnt += 1
