import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))

sum_lst = [lst[0]]

for i in range(len(lst)-1):
    sum_lst.append(max(sum_lst[i]+lst[i+1], lst[i+1]))

print(max(sum_lst))