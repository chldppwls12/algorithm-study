import sys
n = int(sys.stdin.readline())

story = list()

for _ in range(n):
    story.append(list(map(int, sys.stdin.readline().split())))

max_path = [story[0]] + [0] * (n-1)

for i in range(1, n):
    layer = []
    for j in range(len(story[i])):
        if j == 0:
            layer.append(max_path[i-1][j] + story[i][j])
        elif j == len(story[i])-1:
            layer.append(max_path[i-1][j-1] + story[i][j])
        else:
            layer.append(story[i][j] + max(max_path[i-1][j-1], max_path[i-1][j]))
    max_path[i] = layer

print(max(max_path[n-1]))