n = int(input())
t = []
p = []
for i in range(n):
    time, pay = map(int, input().split())
    t.append(time)
    p.append(pay)

dp = [0] * (n + 1)

for i in range(n-1, -1, -1):
    if t[i] > n - i: #상담일이 남은 기간보다 긴 경우
        dp[i] = dp[i+1] #이전 최댓값 저장
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i + t[i]])

print(dp[0])