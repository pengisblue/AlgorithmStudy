# 오등큰수
# 오른쪽에 있으면서 등장횟수가 큰 수

import sys

appear_cnt = [0] * 1_000_001

n = int(input())

numbers = list(map(int, input().split()))

my_stack = []
result = []

for num in numbers:
    appear_cnt[num] += 1

for i in range(n - 1, -1, -1):
    while my_stack and appear_cnt[my_stack[-1]] <= appear_cnt[numbers[i]]:
        my_stack.pop()

    if my_stack:
        result.append(my_stack[-1])
    else:
        result.append(-1)

    my_stack.append(numbers[i])


for i in range(n - 1, -1, -1):
    sys.stdout.write(str(result[i]))
    sys.stdout.write(' ')
