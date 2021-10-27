import random
from datetime import datetime as DT
import time

n = DT.now()

print("now:{}\n".format(n))

start = time.time()

a = random.randint(0, 100)
b = random.randint(0, 100)

ans = int(input("{}+{}=?:".format(a, b)))
end = time.time()
if ans == a+b:
    print("○")
else:
    print("X")

print("Your Time:{}".format(end-start))
