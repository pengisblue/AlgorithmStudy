import sys
input = sys.stdin.readline

N = int(input())

result = []
numbers = []
for _ in range(N):
    commands = input().split()
    command = commands[0]

    if command == 'push':
        # 푸쉬일땐 리스트에 2번째 요소가 있으니까 그거 append해줌
        numbers.append(commands[1])
    elif command == 'pop':
        if len(numbers) > 0:
            result.append(numbers.pop())
        else:
            result.append(-1)
    elif command == 'size':
        result.append(len(numbers))
    elif command == 'empty':
        if len(numbers) == 0:
            result.append(1)
        else:
            result.append(0)
    elif command == 'top':
        if len(numbers) > 0:
            result.append(numbers[-1])
        else:
            result.append(-1)
    
print('\n'.join(map(str,result)))