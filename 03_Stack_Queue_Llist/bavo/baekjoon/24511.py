from collections import deque

# 스택을 쌩까고
# 큐끼리만 큐처럼

n = int(input())

sq = list(map(int, input().split()))
data = list(map(int, input().split()))

m = int(input())

elements = list(map(int, input().split()))

dq = deque()

for i in range(n):
    if not sq[i]:
        dq.append(data[i])

result = []

for i in range(m):
    dq.appendleft(elements[i])
    result.append(dq.pop())

print(*result)

