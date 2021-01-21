#dfs 깊이 우선 탐색
def dfs(v):
    print(v, end =' ')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)

#bfs 너비 우선 탐색


n, m, v = map(int, input().split())
graph = [[0] *(n+1) for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
visit = [0 for i in range(n+1)]
dfs(v)
