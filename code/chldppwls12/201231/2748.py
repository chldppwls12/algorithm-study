# n = int(input())
# def f(n):
#     if n == 0:
#         return 0
#     elif n ==1 or n ==2:
#         return 1
#     return f(n-2) + f(n-1)
# print(f(n))

n = int(input())
f0, f1 = 0, 1
for i in range(n):
    f0, f1 = f1, f0+f1
print(f0)