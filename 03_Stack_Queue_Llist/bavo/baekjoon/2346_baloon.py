from collections import deque

n = int(input())

ballons = list(map(int, input().split()))

my_deque = deque()

for i in range(n):
    my_deque.append((ballons[i], i + 1))

temp_val = 1

result = []

while my_deque:
    while abs(temp_val) > 1:
        if temp_val > 1:
            my_deque.append(my_deque.popleft())
            temp_val -= 1
        elif temp_val < -1:
            my_deque.appendleft(my_deque.pop())
            temp_val += 1

    if temp_val == 1:
        temp_val, temp_index = my_deque.popleft()
    else:
        temp_val, temp_index = my_deque.pop()
    result.append(temp_index)

print(*result)
