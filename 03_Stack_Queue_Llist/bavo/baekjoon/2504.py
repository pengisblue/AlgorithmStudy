bracket = input()

stack = []

curr_value = 1
result = 0

my_dict = {'[': ']', ']': '[', ')': '(', '(': ')'}

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append(bracket[i])
        curr_value *= 2
    elif bracket[i] == '[':
        stack.append(bracket[i])
        curr_value *= 3
    else:
        if not stack or (stack and my_dict[bracket[i]] != stack[-1]):
            print(0)
            break
        if i > 0 and my_dict[bracket[i - 1]] == bracket[i]:
            result += curr_value
        if bracket[i] == ')':
            curr_value //= 2
        else:
            curr_value //= 3
        stack.pop()
else:
    if stack:
        print(0)
    else:
        print(result)
