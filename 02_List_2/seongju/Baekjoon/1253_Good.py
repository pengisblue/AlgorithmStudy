# 1253 - 좋다

import sys

N = int(sys.stdin.readline())
Ai = list(map(int, sys.stdin.readline().split()))


sum_num = 0
sum_list = []
cnt = 0
Ai.sort()


for n in range(N) : # Ai[n] -> 찾을 값
    start = 0
    end = N-1
    
    while start < end :
        sum_num = (Ai[start] + Ai[end])
        if sum_num > Ai[n] :
            end -= 1

        elif sum_num < Ai[n] :
            start += 1

        elif sum_num == Ai[n] :
            if start != n and end != n :
                cnt += 1
                break
            elif start == n :
                start += 1
            elif end == n :
                end -= 1

print(cnt)
