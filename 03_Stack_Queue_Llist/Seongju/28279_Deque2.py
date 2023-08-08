# 덱2
import sys
from collections import deque

input = sys.stdin.readline
d = deque()
N = int(input())

for i in range(N) :
    order = list(map(int, input().split()))

    if order[0] == 1 :
        d.appendleft(order[1])
    elif order[0] == 2 :
        d.append(order[1])
    elif order[0] == 3 :
        if d :
            print(d.popleft())
        else :
            print(-1)
    elif order[0] == 4 :
        if d :
            print(d.pop())
        else :
            print(-1)
    elif order[0] == 5 :
        print(len(d))
    elif order[0] == 6 :
        if not d :
            print(1)
        else :
            print(0)
    elif order[0] == 7 :
        if d :
            print(d[0])
        else :
            print(-1)
    elif order[0] == 8 :
        if d :
            print(d[-1])
        else :
            print(-1)