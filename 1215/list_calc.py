li = []
searcher = ['+','-','*','/','=']
while True:
  i = input("calc :")
  if (not li or not li[-1].isdecimal()) and not i.isdecimal() or (not i .isdecimal() and not i in searcher) or (li and li[-1].isdecimal()) and i.isdecimal():
    print("入力した値が正しくありません")
  elif i == "=":
    break
  else:
    li.append(i)

st = ''.join(li)
print(f'入力した計算式:{st}')
print('計算結果:{}'.format(eval(st)))