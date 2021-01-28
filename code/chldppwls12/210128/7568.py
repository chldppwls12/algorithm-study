n = int(input())
l = []
for i in range(n):
    weight, height = map(int, input().split())
    l.append([weight, height])

for i in range(len(l)):
    rank = 1
    for j in range(len(l)):
        if i != j:
            if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
                rank = rank + 1
    print(rank)