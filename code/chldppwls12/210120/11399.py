n = int(input())
l = list(map(int, input().split()))
l.sort()
time = 0
total = 0
for i in l:
    time = time + i
    total = total + time

print(total)