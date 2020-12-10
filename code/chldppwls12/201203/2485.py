L, P = map(int, input().split())
n = list(map(int, input().split()))
for i in n:
    print(i-L*P,end=' ')