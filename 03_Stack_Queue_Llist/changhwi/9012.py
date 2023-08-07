t = int(input())
for i in range(t):
    stack = []

    n = input()
    for num in n:
        if num == '(':
            stack.append(num)
        #print(stack)
        elif num == ')':
            if stack == []:
                stack.append(num)
                break
            else:
                stack.pop()

    if stack != []:
        print('No')
    else:
        print('Yes')