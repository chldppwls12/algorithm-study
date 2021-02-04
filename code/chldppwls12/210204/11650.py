import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
l.sort()
for i in l:
    print(i[0], i[1])