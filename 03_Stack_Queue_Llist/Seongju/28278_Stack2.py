# 28278 - 스택 2
import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N) :
    order = list(map(int, sys.stdin.readline().split()))

    if len(order) > 1 :
        stack.append(order[1])

    elif len(order) == 1 :
        if order[0] == 2 :
            if not stack :
                print(-1)
            else :
                print(stack.pop())
        elif order[0] == 3 :
            print(len(stack))
        elif order[0] == 4 :
            if not stack :
                print(1)
            else :
                print(0)
        elif order[0] == 5 :
            if not stack :
                print(-1)
            else :
                print(stack[-1])
