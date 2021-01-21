import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
result = [1] * n
for i in range(1, n):
    for j in range(i):
        if l[j] < l[i]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))
