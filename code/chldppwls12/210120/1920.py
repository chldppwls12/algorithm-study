n = int(input())
list_n = list(map(int, input().split()))
list_n.sort()

m = int(input())
list_m = list(map(int, input().split()))

for i in list_m:
    start = 0
    end = n-1
    target = i
    flag = 0
    while start <= end:
        mid = (start + end) //2
        if list_n[mid] == target:
            flag = 1
            break
        elif target < list_n[mid]:
            end = mid - 1
        else:
            start = mid + 1
    print(flag)