import sys
sys.setrecursionlimit(100000)
l = int(input())

def check(i, j, m, n, field):
    # 위 체크
    if i-1 >= 0 and field[i-1][j] == 1:
        field[i-1][j] += 1
        check(i-1, j, m, n, field)
    
    # 아래 체크
    if i+1 <= m-1 and field[i+1][j] == 1:
        field[i+1][j] += 1
        check(i+1, j, m, n, field)
    
    # 왼쪽 체크
    if j-1 >= 0 and field[i][j-1] == 1:
        field[i][j-1] += 1
        check(i, j-1, m, n, field)
    
    # 오른쪽 체크
    if j+1 <= n-1 and field[i][j+1] == 1:
        field[i][j+1] += 1
        check(i, j+1, m, n, field)


for _ in range(l):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1
    count = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                count += 1
                field[i][j] += 1
                check(i, j, m, n, field)

    print(count)