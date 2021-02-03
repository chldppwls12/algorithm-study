from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i-1][j-1] = 1
    graph[j-1][i-1] = 1

point = deque(list(range(n)))
count = 0

while point:
    count += 1
    index = point.popleft()
    visited = [index]
    wait = deque([])
    for i, check in enumerate(graph[index]):
        if check == 1:
            wait.append(i)
            point.remove(i)

    while wait:
        index = wait.popleft()
        visited.append(index)
        for i, check in enumerate(graph[index]):
            if check == 1 and i not in wait and i not in visited:
                wait.append(i)
                point.remove(i)

print(count)