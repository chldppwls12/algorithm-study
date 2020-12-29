import sys
n = int(input())

for i in range(n):
    stack = list()
    lst = sys.stdin.readline().strip()
    for j, bracket in enumerate(lst):
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                print('NO')
                break
            else:
                stack.pop()
        
        if j == len(lst)-1 and stack:
            print('NO')
            break
    else:
        print('YES')