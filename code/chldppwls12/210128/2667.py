def dfs(x, y):
    global ctn
    if x <= -1 or x >=n or y <= -1 or y >=n:
        return False
    if graph[x][y] == 1:
        ctn = ctn + 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int ,input())))

ctn = 0
result = 0
house = []

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result = result + 1
            house.append(ctn)
            ctn = 0
print(result)
house.sort()
for i in house:
    print(i)
