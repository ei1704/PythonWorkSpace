str1 = "abcdef"
idx = len(str1) - 1
while idx >= 0:
    print(str1[idx])
    idx -= 1

# 別解
length = len(str1)
for i in range(length):
    print(str1[length-i-1])

for i in reversed(str1):
    print(i)

idx2 = -1
while idx2 >= -len(str1):
    print(str1[idx2])
    idx2 -= 1
