import sys
n = int(input())

people = []
for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    people.append([weight, height, 1])

for person in people:
    for compare in people:
        if person[0] < compare[0] and person[1] < compare[1]:
            person[2] += 1

for person in people:
    print(person[2], end=' ')