print("偶数一覧")
print("=>", end="")
for i in range(2, 100, 2):
    print(i, end=",")

# 別解
#result = [i*2 for i in range(1, 50)]
# print(f'偶数一覧=>{result}')
