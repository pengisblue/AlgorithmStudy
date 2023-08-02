# 수들의 합 5

import sys

N = int(sys.stdin.readline())
count = 0

for start in range(1, N+1) :    # 1~N까지
    sum_N = 0
    end = start
    while sum_N < N and end < N+1 :
        sum_N += end
        end += 1
        
    if sum_N == N :
        count += 1

print(count)