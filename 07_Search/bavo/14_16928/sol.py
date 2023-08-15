from collections import deque
import sys

input = sys.stdin.readline

board = [-1] * 101
board[1] = 0

ladder = dict()

N, M = map(int, input().split())

for _ in range(N + M):
    x, y = map(int, input().split())
    ladder[x] = y

queue = deque()
queue.append(1)

while queue:
    curr = queue.popleft()
    if curr == 100:
        break

    for i in range(1, 7):
        target = i + curr
        if target <= 100:
            if target in ladder:
                target = ladder[target]
            if board[target] == -1:
                board[target] = board[curr] + 1
                queue.append(target)


print(board[100])
