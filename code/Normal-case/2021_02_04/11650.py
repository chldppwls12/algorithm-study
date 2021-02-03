import sys
n = int(input())

coordinate = list()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append((x, y))

coordinate = sorted(coordinate, key=lambda x:(x[0], x[1]))

for point in coordinate:
    print(point[0], point[1])