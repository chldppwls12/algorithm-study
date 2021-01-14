n = int(input())

lst = []
while n//10 != 0:
    lst.append(n%10)
    n = n//10
lst.append(n%10)

lst.sort(reverse=True)

for i in lst:
    print(i, end='')