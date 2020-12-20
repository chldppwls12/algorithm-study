import sys
n = int(input())
line = list()
for _ in range(n):
    line.append(int(sys.stdin.readline()))

for i in sorted(line):
    print(i)