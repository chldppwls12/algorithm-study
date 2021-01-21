import sys

n = int(sys.stdin.readline())

dic = dict()
num = list(map(int, sys.stdin.readline().split()))

for i in num:
    dic[i] = 1

m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

for i in check:
    try:
        dic[i] += 1
        print(1)
    except:
        print(0)