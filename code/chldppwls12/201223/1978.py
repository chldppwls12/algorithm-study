import sys
n = int(input())
nums = list(map(int,sys.stdin.readline().split()))
ctn = 0
for i in nums:
    for j in range(2, i+1):
        if i % j ==0:
            if i!=j:
                break
            else:
                ctn = ctn+1
print(ctn)