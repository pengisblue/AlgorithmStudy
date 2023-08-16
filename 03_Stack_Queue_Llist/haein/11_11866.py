N, K = map(int, input().split())
numbers = list(range(1, N+1))
idx = 0
result = []
while numbers:
    idx += K - 1
    if idx >= len(numbers):
        idx = (idx-len(numbers)) % len(numbers)
    result.append(str(numbers.pop(idx)))

print('<', ', '.join(map(str, result)), '>', sep='')
