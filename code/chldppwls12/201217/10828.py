import sys
n = int(sys.stdin.readline())
l = []

def push(n):
    l.append(n)

def pop():
    if l:
        return l.pop()
    else:
        return -1

def size():
    return len(l)

def empty():
    if l:
        return 0
    else:
        return 1

def top():
    if l:
        return l[-1]
    else:
        return -1

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        print(pop())
    elif order[0] == 'size':
        print(size())
    elif order[0] =='empty':
        print(empty())
    elif order[0] == 'top':
        print(top())
