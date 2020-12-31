n = int(input())
for i in range(n):
    ctn =0
    total =0
    s = input()
    for j in s:
        if j == 'O':
            ctn = ctn + 1
            total = total + ctn
        elif j == 'X':
            ctn = 0
            total = total + ctn
    print(total)
