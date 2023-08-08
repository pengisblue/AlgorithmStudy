# 균형잡힌 세상
import sys

while True :
    sentence = list(map(str, sys.stdin.readline().rstrip()))

    if sentence[0] == '.' :
        break

    stack_s = []
    for i in range(len(sentence)) :
        if sentence[i] == '(' or sentence[i] == '[':
            stack_s.append(sentence[i])
        elif sentence[i] == ')':
            if stack_s and stack_s[-1] == '(':
                stack_s.pop()
            else :
                stack_s.append(0)
                break
        elif sentence[i] == ']':
            if stack_s and stack_s[-1] == '[':
                stack_s.pop()
            else:
                stack_s.append(0)
                break

    if not stack_s:
        print('yes')
    else :
        print('no')
