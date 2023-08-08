import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numbers = deque(range(N, 0, -1))
while len(numbers) > 1:
    numbers.pop()
    numbers.appendleft(numbers.pop())

print(*numbers)