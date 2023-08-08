# 12789 - 도키도키 간식 드리미
import sys

N = int(sys.stdin.readline())
A = list(map(int, reversed(sys.stdin.readline().split())))
min_A = 1
max_A = len(A)
stack = []

while min_A <= max_A :
    if A and A[-1] == min_A :
        A.pop()
        min_A += 1
    else :
        if stack :
            if stack[-1] == min_A :
                stack.pop()
                min_A += 1
            elif A :
                stack.append(A.pop())
            else :
                break
        else :
            stack.append(A.pop())

if stack :
    print('Sad')
elif not stack :
    print('Nice')