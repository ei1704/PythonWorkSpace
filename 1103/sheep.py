import time

n = int(input("何匹数えますか？:"))
for i in range(1, n+1):
    print("羊が{}匹".format(i))
    time.sleep(1)
