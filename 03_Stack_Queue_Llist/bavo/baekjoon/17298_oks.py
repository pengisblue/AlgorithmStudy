# 오큰수 스택으로
import sys

n = int(input())

numbers = list(map(int, input().split()))

my_stack = []
result = []
for i in range(n - 1, -1, -1):
    while my_stack and my_stack[-1] <= numbers[i]:
        my_stack.pop()

    if my_stack:
        result.append(my_stack[-1])
    else:
        result.append(-1)

    my_stack.append(numbers[i])

for i in range(n - 1, -1, -1):
    sys.stdout.write(str(result[i]))
    sys.stdout.write(' ')
