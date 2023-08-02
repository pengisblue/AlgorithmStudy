# 1940 - 주몽

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

cnt = 0
start = 0
end = N-1

T.sort()

while start < end:
    current_sum = T[start] + T[end]
    if current_sum == M:
        cnt += 1
        start += 1
        end -= 1
    elif current_sum < M:
        start += 1
    else:
        end -= 1

print(cnt)
