import sys
input = sys.stdin.readline


N = int(input())
for _ in range(N):
    brackets = list(input())
    stack = []
    VPS = True
    for i in range(len(brackets)-1):
        if brackets[i] == '(':
            stack.append('(')
        else:
            if not stack:
                VPS = False
                break
            else:
                stack.pop()

    if stack:
        VPS = False

    if VPS:
        print('YES')
    else:
        print('NO')
