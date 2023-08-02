from collections import deque

d = deque()

N, L = map(int, input().split()) 

numbers = list(map(int, input().split()))

# 값, 인덱스
for i in range(N):
    while d and d[-1][0] > numbers[i]:
        d.pop()
    if d and d[0][1] < i - L + 1:
        d.popleft()
    d.append((numbers[i], i))
    # print(d)
    print(d[0][0], end=' ')


