# 문자열 폭발
# 아직 못품

from collections import deque


def bomb(stack, bomb):
    stack_index = len(stack) - 1
    for i in range(bomb_len):
        if stack[stack_index] != bomb[bomb_len - 1 - i]:
            return
        stack_index -= 1

    for i in range(bomb_len):
        stack.pop()


original_str = input()

bomb_str = input()

bomb_len = len(bomb_str)

result = []

for i in range(len(original_str)):
    result.append(original_str[i])

    if original_str[i] == bomb_str[-1] and len(result) >= bomb_len:
        bomb(result, bomb_str)

if result:
    print(*result, sep='')
else:
    print('FRULA')
