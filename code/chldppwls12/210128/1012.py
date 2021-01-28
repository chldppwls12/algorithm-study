import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x <= -1 or x >= n or y <=-1 or y >= m:
        return False
    #현재 위치에 배추가 있으면
    if graph[x][y] == 1:
        graph[x][y] = 0 #현재 위치의 탐색을 완료했으므로 0으로 바꾸기
        dfs(x - 1, y)
        dfs(x, y-1)
        dfs(x + 1, y)
        dfs(x, y+1)
        #배추 주변에 있는 인접한 배추들 모두 방문 후 true 반환
        return True
    #현재 위치에 배추가 없으면 false 반환
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
            #현재 위치에서 DFS 수행/ 현재 위치가 배추 밀집 지역이면
            if dfs(i, j) == True:
                ctn = ctn + 1
    result.append(ctn)

for i in result:
    print(i)