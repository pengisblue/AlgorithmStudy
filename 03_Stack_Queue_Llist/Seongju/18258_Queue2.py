# 큐 2
import sys
from collections import deque
input = sys.stdin.readline

que = deque()
N = int(input())
for i in range(N) :
    order = list(map(str, input().split()))

    if order[0] == 'push' :
        que.append(order[1])
    elif order[0] == 'pop' :
        if que :
            print(que.popleft())
        else :
            print(-1)
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if not que :
            print(1)
        else :
            print(0)
    elif order[0] == 'front':
        if que :
            print(que[0])
        else :
            print(-1)
    elif order[0] == 'back':
        if que :
            print(que[-1])
        else :
            print(-1)

