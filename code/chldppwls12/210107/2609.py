#유클리드 호제법 (a와 b의 최대공약수는 b와 a%b의 최대공약수와 같다)
A, B = map(int, input().split())
a, b = A, B
while b != 0:
    a = a % b
    a, b = b, a

print(a)
print(A*B//a)