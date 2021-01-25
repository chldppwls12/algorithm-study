# n = int(input())
# count = 0
# while True:
#     if a== 1:
#         print(count)
#         break
#     if a%3 ==0:
#         a = a/3
#     elif a%2 == 0:
#         a = a/2
#     else:
#         a = a-1
#     count = count +1

#다이나믹 프로그래밍
#dp[N] = min(dp[N-1], dp[N//2] , dp[N//3]) + 1
n = int(input())
dp = [0,0,1,1]
for i in range(4, n+ 1):
    dp.append(dp[i-1]+1)
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 ==0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[-1])
