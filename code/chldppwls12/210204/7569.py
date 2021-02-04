# from collections import deque
# import sys

# dx = [1, -1, 0, 0, 0, 0]
# dy = [0, 0, 1, -1, 0, 0]
# dz = [0, 0, 0, 0, 1, -1]

# def bfs():
#     while queue:
#         x, y, z = queue.popleft()
#         for i in range(6):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nz = z + dz[i]
#             if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
#                 if arr[nx][ny][nz] == 0 and c[nx][ny][nz] == 0:
#                     queue.append([nx, ny, nz])
#                     arr[nx][ny][nz] = 1
#                     c[nx][ny][nz] = c[x][y][z] + 1

# m, n, h = map(int, input().split())
# arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# c = [[[0]*m for _ in range(n)] for _ in range(h)]
# queue = deque()

# for i in range(h):
#     for j in range(n):
#         for l in range(m):
#             if arr[i][j][l] == 1 and c[i][j][l] == 0:
#                 queue.append([i, j, l])
#                 c[i][j][l] = 1

# bfs()

# for i in arr:
#     for j in i:
#         if 0 in j:
#             print(-1)
#             sys.exit()
# ans = 0
# for i in c:
#     for j in i:
#         list_max = max(j)
#         ans = max(ans, list_max)
# print(ans-1)


