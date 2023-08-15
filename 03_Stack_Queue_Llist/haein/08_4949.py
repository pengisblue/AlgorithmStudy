from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def is_balance(text):
    stack = deque()
    if text[-1] != '.':
        return 'no'
    for alpha in text:
        if alpha == '(' or alpha == '[':
            stack.append(alpha)
        elif alpha == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'no'
        elif alpha == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return 'no'

    if stack:
        return 'no'
    else:
        return 'yes'


while True:
    text = input().rstrip()
    if text == '.':
        break
    print(is_balance(text))
