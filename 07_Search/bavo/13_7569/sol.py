from collections import deque

import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())

queue = deque()

tomato_tower = []

for height in range(H):
    tomato_box = []
    for i in range(N):
        tomato_line = list(map(int, input().split()))
        for j in range(M):
            if tomato_line[j] == 1:
                queue.append((height, i, j))
        tomato_box.append(tomato_line)
    tomato_tower.append(tomato_box)

while queue:
    z, x, y = queue.popleft()

    for k in range(6):
        nz, nx, ny = z + dz[k], x + dx[k], y + dy[k]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomato_tower[nz][nx][ny] == 0:
            tomato_tower[nz][nx][ny] = tomato_tower[z][x][y] + 1
            queue.append((nz, nx, ny))

max_val = 0

for box in tomato_tower:
    for line in box:
        if 0 in line:
            print(-1)
            sys.exit()
        else:
            max_val = max(max_val, max(line))

print(max_val - 1)
