# 2164 - 카드2
import sys
from collections import deque

deq = deque()
N = int(sys.stdin.readline())

for i in range(N, 0, -1) :
    deq.append(i)

while len(deq) > 1 :
    deq.pop()
    deq.appendleft(deq.pop())


print(deq[0])
