import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x <= -1 or x >= n or y <=-1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y-1)
        dfs(x + 1, y)
        dfs(x, y+1)
        return True
    return False

test = int(input())
result = []
for _ in range(test):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    ctn = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                ctn = ctn + 1
    result.append(ctn)

for i in result:
    print(i)