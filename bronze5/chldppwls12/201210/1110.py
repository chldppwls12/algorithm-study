n = int(input())
cnt = 0
check = n
while True:
    cnt = cnt + 1
    ten = n//10
    one = n%10
    each_sum = ten + one
    new = one * 10 + each_sum % 10
    n = new
    if check == new:
        break

print(cnt)
