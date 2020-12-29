import sys

n = int(input())
for i in range(n):
    lst = list(map(int, sys.stdin.readline().strip().split(' ')))[1:]
    average = sum(lst) / len(lst)
    for j, score in enumerate(sorted(lst, reverse=True)):
        if score <= average:
            print('{:.3f}%'.format((j)/len(lst)*100))
            break