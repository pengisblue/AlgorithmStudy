import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
now = 1     # 현재 순서
wait = []
result = 'Nice'
while now < N:
    if numbers and numbers[0] == now:
        numbers.pop(0)
        now += 1
    else:
        if wait and wait[-1] == now:
            wait.pop()
            now += 1
        elif numbers:
            wait.append(numbers.pop(0))
        else:
            result = 'Sad'
            break

print(result)
