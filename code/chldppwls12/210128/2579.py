n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

if n == 1:
    print(l[0])
elif n ==2:
    print(max(l[0]+l[1], l[1]))
else:
    dp = []
    dp.append(l[0])
    dp.append(max(l[0]+l[1], l[1]))
    dp.append(max(l[0]+ l[2], l[1]+ l[2]))
    for i in range(3, n):
        #end-2 계단을 밟은 경우 => dp[i-2] + 마지막 계단
        #end-1인 경우 end-2 계단을 밟으면 안됨 => dp[i-3] + i-1 계단 + 마지막 계단
        dp.append(max(dp[i-2]+ l[i], dp[i-3]+l[i-1]+l[i]))
    print(dp[-1])
