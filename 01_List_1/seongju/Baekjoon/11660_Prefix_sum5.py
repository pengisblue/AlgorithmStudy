# 구간 합 구하기 5

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = [[0] * (N+1)]
D = [[0] * (N+1) for _ in range(N+1)]

for n in range(N) :
    row = [0] + [int(x) for x in input().split()]
    print(row)
    array.append(row)
    
for i in range(1, N+1) :
    for j in range(1, N+1) :
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + array[i][j]          
    
for m in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    answer = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(answer)