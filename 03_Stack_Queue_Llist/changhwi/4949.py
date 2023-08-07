while True:

    str = input()
    stack = []

    if str == ".":
        break

    for i in str:
        if i == '(':
            stack.append('(')
        elif i == '[':
            stack.append('[')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if len(stack) == 0:
                stack.append(']')
                break
            elif stack[-1] == '[':
                stack.pop()

    if len(stack) != 0:
        print('no')
    else:
        print('yes')




