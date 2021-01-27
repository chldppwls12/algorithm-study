import sys
n = int(input())

lst = [0] * 300
for i in range(n):
    lst[i] = int(sys.stdin.readline())
    
dynamic = [0] * 300
dynamic[0] = lst[0]
dynamic[1] = lst[0]+lst[1]
dynamic[2] = max(lst[0]+lst[2], lst[1]+lst[2])

if n > 3:
    for i in range(3, n):
        dynamic[i] = max(dynamic[i-3] + lst[i-1] + lst[i], dynamic[i-2] + lst[i])

print(dynamic[n-1])