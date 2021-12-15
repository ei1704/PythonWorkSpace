import math

def input_init(message):
  a = input(message+":")
  if a.isdecimal():
    a = int(a)
  else:
    a = 0
  return a

def calc_payment(val,pep):
  res = {"支払金額":math.ceil(val/(pep*100))*100}
  res["幹事金額"] = val - (pep -1) * res["支払金額"]
  return res

def output_payment(one_pay,re_pay,pep):
  print("支払金額:{:,}円({}人)".format(one_pay,pep-1))
  print("幹事金額:{:,}円".format(re_pay))

sum_val = input_init("支払合計金額を入力してください")
sum_pep = input_init("参加者人数を入力してください")
pay = calc_payment(sum_val, sum_pep)
output_payment(pay["支払金額"],pay["幹事金額"],sum_pep)