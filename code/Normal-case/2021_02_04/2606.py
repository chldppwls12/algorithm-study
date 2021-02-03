from collections import deque
import sys

computer = int(input())
connect = int(input())

network = [[0 for _ in range(computer)] for _ in range(computer)]

for _ in range(connect):
    i, j = map(int, sys.stdin.readline().split())
    network[i-1][j-1] = 1
    network[j-1][i-1] = 1

womb = [0]
queue = deque([])


for i, check in enumerate(network[0]):
    if check == 1:
        queue.append(i)
        
while queue:
    index = queue.popleft()
    womb.append(index)
    for i, check in enumerate(network[index]):
        if check == 1 and i not in womb and i not in queue:
            queue.append(i)

print(len(womb)-1)