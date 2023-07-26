N, k = map(int,input().split())
numbers = [num for num in range(1, N+1)]
result = ['<','>']
index = k - 1
cnt = 1

while len(numbers) > 0:
    if len(numbers) == 1:
        n = numbers.pop()
        result.insert(cnt, f'{n}')
        break
    if index >= len(numbers):
        index %= len(numbers)
    n = numbers.pop(index)
    result.insert(cnt, f'{n}, ')
    index += k - 1
    cnt += 1

print(*result, sep='')