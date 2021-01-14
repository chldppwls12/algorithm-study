n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    long_dist, short_dist = max(r1, r2), min(r1, r2)

    if distance > r1 + r2:
        print(0)
    elif distance == r1 + r2:
        print(1)
    else:
        if distance + short_dist > long_dist:
            print(2)
        elif distance + short_dist == long_dist and distance != 0:
            print(1)
        else:
            if x1 == x2 and y1 == y2 and r1 == r2:
                print(-1)
            else:
                print(0)