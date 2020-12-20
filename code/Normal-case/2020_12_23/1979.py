import sys
n = int(input())
line = list(map(int, sys.stdin.readline().split(' ')))

# False = 소수 아님 True = 소수
prime = [False, False] + [True] * 1000

# prime number count
count = 0

'''
특정 숫자의 소수를 확인하기 위해서는 1 또는 자기자신 이외에 나누어지는 숫자가 있는지 확인한다.
하지만 숫자 100의 경우 2, 3, 4, 5 ... 모든 숫자를 확인하는 것은 비효율적이다.
따라서 에라토스테네스 체 알고리즘을 사용한다. 먼저 숫자 100의 경우
2 ~ 10(100의 제곱근)까지만 확인하면 소수인지 판별 가능하다.
또 2를 확인한 후 4, 6, 8, 10을 확인하는 것은 비효율적이므로 2를 확인하는 동시에
4, 6, 8, 10을 걸러준다.
'''
# Sieve of Eratosthenes(에라토스테네스 체)
for i, number in enumerate(line):
    # 1은 소수 아니라서 패스
    if number == 1: continue

    # 소수 확인은 2부터 자기자신의 제곱근까지만 확인하면 됨
    for j in range(2, int(number**0.5) + 1):

        if prime[j]:
            if number%j==0:
                break
            
            # 체로 걸러주는 부분
            for k in range(2*j, int(number**0.5) + 1, j):
                prime[k] = False
    # 따로 break가 되지않고 for문을 다 돌면 소수로 판별
    else: count += 1
print(count)