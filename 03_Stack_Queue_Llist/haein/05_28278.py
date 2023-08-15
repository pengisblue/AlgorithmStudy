import sys
input = sys.stdin.readline


def stack(lst, num1, num2=None):
    if num1 == 1:
        lst.append(num2)
    elif num1 == 2:
        if my_stack:
            print(lst.pop())
        else:
            print(-1)
    elif num1 == 3:
        print(len(lst))
    elif num1 == 4:
        if my_stack:
            print(0)
        else:
            print(1)
    elif num1 == 5:
        if my_stack:
            print(lst[-1])
        else:
            print(-1)


N = int(input())
my_stack = []
for i in range(N):
    stack(my_stack, *list(map(int, input().split())))
