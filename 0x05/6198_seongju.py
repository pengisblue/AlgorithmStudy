import sys

buildings = []
N = int(sys.stdin.readline())

for i in range(N) :
    buildings.append(int(sys.stdin.readline()))

stack = []
answer = 0

for b in buildings :
    while stack and stack[-1] <= b :
        stack.pop()
    stack.append(b)
    answer += len(stack) - 1

print(answer)