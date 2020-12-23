n = int(input())
score = list(map(int, input().split()))
maxScore = max(score)
newScore = []
for i in score:
    newScore.append(i/maxScore*100)
avg = sum(newScore)/n
print(avg)