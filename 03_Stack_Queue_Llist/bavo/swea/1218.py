bracket_dict = {'{': '}', '(': ')', '[': ']', '<': '>'}

for T in range(1, 11):
    stack = []
    size = int(input())
    brackets = input()
    valid = True
    for i in range(size):
        if brackets[i] in bracket_dict:
            stack.append(brackets[i])
        else:
            if not stack or bracket_dict[stack[-1]] != brackets[i]:
                valid = False
                break
            stack.pop()
    if stack:
        valid = False

    print(f'#{T} {int(valid)}')


