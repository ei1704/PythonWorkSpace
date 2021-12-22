import datetime
def log_file(func):
  def funcname(*args,**kwargs):
    result = func(*args,**kwargs)
    dt_now = datetime.datetime.now()
    with open('files/python.log', 'a', encoding='utf-8', newline='\n') as f:
      f.write(f"{dt_now} function:{func.__name__} args:{args} kwargs:{kwargs}\n")
    return result
  return funcname

# main
@log_file
def test(n):
 print('test->{}'.format(n))
# 呼出
test(100)
# 呼出
for i in range(5):
 test(i)
