import sys
n = int(input())

a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

s = 0
for i, j in zip(a, b):
    s += i*j

print(s)