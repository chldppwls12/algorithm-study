import sys
n = int(input())
line = list(map(int, sys.stdin.readline().split(' ')))

max_value = max(line)
average = sum(line) / max_value * 100 / n
print(average)