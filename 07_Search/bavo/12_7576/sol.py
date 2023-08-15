import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())

tomatoes = []

queue = deque()

for i in range(N):
    tomato_line = list(map(int, input().split()))
    tomatoes.append(tomato_line)
    for j in range(M):
        if tomato_line[j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
            tomatoes[nx][ny] = tomatoes[x][y] + 1
            queue.append((nx, ny))

max_val = 0
for line in tomatoes:
    if 0 in line:
        print(-1)
        break

    max_val = max(max_val, *line)
else:
    print(max_val - 1)
