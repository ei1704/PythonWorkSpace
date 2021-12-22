import time
def run_time(func):
  def funcname(*args,**kwargs):
    start = time.time()
    result = func(*args,**kwargs)
    end = time.time() - start
    print(f"実行関数:{func.__name__} 実行時間:{end}")
    return result
  return funcname
# main
@run_time
def test(n):
  for i in range(n):
    time.sleep(i)

test(3)
test(5)