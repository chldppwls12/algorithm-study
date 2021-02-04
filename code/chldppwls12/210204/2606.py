from collections import deque

n = int(input())
connect = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(connect):
    y, x = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque()
queue.extend(graph[1])
visited = [False] * (n + 1)
visited[1] = True
answer = 0

while queue:
    v = queue.popleft()
    if visited[v] is False:
        answer = answer + 1
        queue.extend(graph[v])
        visited[v] = True
print(answer)