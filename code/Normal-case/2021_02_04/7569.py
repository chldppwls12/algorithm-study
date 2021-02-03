from collections import deque
import sys
m, n, h = map(int, sys.stdin.readline().split())

tomato = [[[0 for _ in range(h)] for _ in range(n)] for _ in range(m)]
wait = deque(list())
for k in range(h):
    for j in range(n):
        x_lst = list(map(int, sys.stdin.readline().split()))
        for i, status in enumerate(x_lst):
            tomato[i][j][k] = status
            if status == 1:
                wait.append((i, j, k))

day = -1

while wait:
    day += 1
    loop = len(wait)
    for _ in range(loop):
        index = wait.popleft()

        # 위
        if index[2] < h-1 and tomato[index[0]][index[1]][index[2]+1] == 0:
            wait.append((index[0], index[1], index[2]+1))
            tomato[index[0]][index[1]][index[2]+1] = 1
        
        # 아래
        if 0 < index[2] and tomato[index[0]][index[1]][index[2]-1] == 0:
            wait.append((index[0], index[1], index[2]-1))
            tomato[index[0]][index[1]][index[2]-1] = 1

        # 앞
        if index[1] < n-1 and tomato[index[0]][index[1]+1][index[2]] == 0:
            wait.append((index[0], index[1]+1, index[2]))
            tomato[index[0]][index[1]+1][index[2]] = 1
        
        # 뒤
        if 0 < index[1] and tomato[index[0]][index[1]-1][index[2]] == 0:
            wait.append((index[0], index[1]-1, index[2]))
            tomato[index[0]][index[1]-1][index[2]] = 1

        if index[0] < m-1 and tomato[index[0]+1][index[1]][index[2]] == 0:
            wait.append((index[0]+1, index[1], index[2]))
            tomato[index[0]+1][index[1]][index[2]] = 1
        
        if 0 < index[0] and tomato[index[0]-1][index[1]][index[2]] == 0:
            wait.append((index[0]-1, index[1], index[2]))
            tomato[index[0]-1][index[1]][index[2]] = 1

not_complete = False
for k in range(h):
    for j in range(n):
        for i in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                not_complete = True
                break
        else:
            continue
        break
    else:
        continue
    break
if not not_complete:
    print(day)