import sys
n = int(input())

dic = dict()
for _ in range(n):
    value = int(sys.stdin.readline())
    try:
        dic[value] += 1
    except:
        dic[value] = 1

for i in range(10001):
    if i in dic:
        for _ in range(dic[i]):
            print(i)