# Prefix_sum_4

import sys
M, N = (map(int, sys.stdin.readline().split()))

T = list(map(int, sys.stdin.readline().split()))
sum_t = 0 
prefix_sum = [0]

for t in T :
    sum_t += t
    prefix_sum.append(sum_t)


for n in range(N) :
    min_n, max_n = map(int,sys.stdin.readline().split())
    
    answer = prefix_sum[max_n] - prefix_sum[min_n - 1]
    print(answer)