num = list(map(int, input().split()))
sum = 0
for i in num:
    sum = sum + i*i
print(sum%10)