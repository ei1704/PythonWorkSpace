import math

def input_init(message):
  a = input(message+":")
  return int(a)

def calc_payment(val,pep):
  avg = val/pep
  a,b=divmod(avg,100)
  a*=100
  res = {"支払金額":int(a)}
  if b > 0: 
    res["支払金額"]+=100
  res["幹事金額"] = int(val - (pep -1) * res["支払金額"])
  return res

def output_payment(one_pay,re_pay,pep):
  print("支払金額:{:,}円({}人)".format(one_pay,pep-1))
  print("幹事金額:{:,}円".format(re_pay))

sum_val = input_init("支払合計金額を入力してください")
sum_pep = input_init("参加者人数を入力してください")
pay = calc_payment(sum_val, sum_pep)
output_payment(pay["支払金額"],pay["幹事金額"],sum_pep)