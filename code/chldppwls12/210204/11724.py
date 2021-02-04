import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    y, x = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

answer = 0
for i in range(1, n+1):
    if visited[i] is False:
        bfs(graph, i, visited)
        answer = answer + 1

print(answer)