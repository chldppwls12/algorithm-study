import sys
sys.setrecursionlimit(100000)

def check(i, j, n, field, lst):
    lst.append((i, j))
    # 위 체크
    if i-1 >= 0 and field[i-1][j] == 1:
        field[i-1][j] += 1
        check(i-1, j, n, field, lst)
    
    # 아래 체크
    if i+1 <= n-1 and field[i+1][j] == 1:
        field[i+1][j] += 1
        check(i+1, j, n, field, lst)
    
    # 왼쪽 체크
    if j-1 >= 0 and field[i][j-1] == 1:
        field[i][j-1] += 1
        check(i, j-1, n, field, lst)
    
    # 오른쪽 체크
    if j+1 <= n-1 and field[i][j+1] == 1:
        field[i][j+1] += 1
        check(i, j+1, n, field, lst)


n = int(input())
apartment = [list(map(int, input())) for _ in range(n)]

group = 0
element = list()
for i in range(n):
    for j in range(n):
        if apartment[i][j] == 1:
            lst = []
            group += 1
            apartment[i][j] += 1
            check(i, j, n, apartment, lst)
            element.append(len(lst))
element.sort()
print(group)
for e in element:
    print(e)