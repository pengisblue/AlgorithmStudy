# 괄호
import sys

T = int(sys.stdin.readline())
for t in range(1, T+1) :
    ls = list(map(str, sys.stdin.readline().rstrip()))
    stack = []

    for i in range(len(ls)) :
        if ls[i] == '(' :
            stack.append(ls[i])
        elif ls[i] == ')' :
            if not stack :
                stack.append(0)
                break
            else :
                stack.pop()

    if not stack :
        print('YES')
    else :
        print('NO')