import sys
n = int(input())
line = list()
for _ in range(n):
    line.append(sys.stdin.readline().strip().split(' '))

for line_element in line:
    print(sum(map(int, line_element)))