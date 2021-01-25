import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()

time = [lst[0]] + [0] * (len(lst)-1)
for i in range(1, len(lst)):
    time[i] = time[i-1] + lst[i]


print(sum(time))