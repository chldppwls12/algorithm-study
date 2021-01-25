import sys
n = int(sys.stdin.readline())
lst = [0] + list(map(int, sys.stdin.readline().split()))
dynamic = [0] * (len(lst))

for i in range(1, len(lst)):
    max_value = 0
    for j in range(i):
        if lst[j] < lst[i] and dynamic[j] > max_value:
            max_value = dynamic[j]
    dynamic[i] = max_value + 1

print(max(dynamic))