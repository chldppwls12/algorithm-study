n = int(input())
for i in range(n):
    l = list(input())
    ctn = 0
    while(len(l) != 0):
        if l[0] == ')':
            print('NO')
            break
        else:
            if ')' in l:
                l.remove(')')
                l.remove('(')
            else:
                print('NO')
                break
    if len(l) == 0:
        print('YES')