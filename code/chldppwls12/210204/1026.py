n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse= True)
b.sort()
ctn = 0
for i in range(n):
    ctn = ctn + a[i]*b[i]
print(ctn)