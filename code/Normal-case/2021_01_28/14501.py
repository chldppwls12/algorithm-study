import sys
n = int(input())

lst = list()
for _ in range(n):
    duration, profit = map(int, sys.stdin.readline().split())
    lst.append((duration, profit))

lst.append((0, 0))
max_profit = [0] * (n+1)
for i, consult in enumerate(lst[::-1]):
    if i == 0: continue

    if i >= consult[0]:
        max_value = consult[1] + max_profit[i-consult[0]]
        for j in range(1, consult[0]):
            if max_value < max_profit[i-j]:
                max_value = max_profit[i-j]
        max_profit[i] = max_value
    else:
        max_profit[i] = max_profit[i-1]

print(max(max_profit))