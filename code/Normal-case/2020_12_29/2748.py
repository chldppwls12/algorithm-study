n = int(input())
previous, present = 0, 1

for i in range(n):
    previous, present = present, previous + present

print(previous)