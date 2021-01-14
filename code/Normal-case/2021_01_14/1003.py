t = int(input())

for _ in range(t):
    n = int(input())
    
    output = [[1, 0], [0, 1]] + [0] * 40
    
    for i in range(2, n+1):
        output[i] = [output[i-1][0]+output[i-2][0], output[i-1][1]+output[i-2][1]]
    
    print(f'{output[n][0]} {output[n][1]}')