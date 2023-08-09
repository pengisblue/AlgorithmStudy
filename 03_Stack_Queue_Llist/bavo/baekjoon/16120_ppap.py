def ppap(arr):
    ppap_len = len(arr)
    if ppap_len >= 4 and arr[-1] == 'P' and arr[-2] == 'A' and arr[-3] == 'P' and arr[-4] == 'P':
        for _ in range(3):
            arr.pop()


ppap_string = input()

stack = []

for p in ppap_string:
    stack.append(p)
    if p == 'P':
        ppap(stack)

if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')