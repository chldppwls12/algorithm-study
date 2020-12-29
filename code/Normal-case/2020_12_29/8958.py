import sys
n = int(input())

for i in range(n):
    lst = sys.stdin.readline().strip().split('X')
    result = 0
    for lst_length in lst:
        result += sum(range(1, len(lst_length)+1))
    print(result)