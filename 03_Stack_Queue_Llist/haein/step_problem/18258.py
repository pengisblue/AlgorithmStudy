from collections import deque
import sys
input = sys.stdin.readline


def command(q, com, num=None):
    if com == 'push':
        q.append(int(num))
    elif com == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif com == 'size':
        print(len(q))
    elif com == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif com == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif com == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)


N = int(input())
my_queue = deque([])
for i in range(N):
    com = input().split()
    command(my_queue, *com)
