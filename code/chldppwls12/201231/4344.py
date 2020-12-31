c = int(input())
for i in range(c):
    ctn = 0
    n = list(map(int, input().split()))
    avg = sum(n[1:]) / n[0]
    for j in n[1:]:
        if j > avg:
            ctn = ctn + 1
    percent = ctn/n[0] * 100
    print(f'{percent:.3f}%')
