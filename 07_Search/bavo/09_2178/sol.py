# 미로 탐색
# 너비 우선 탐색
# 큐에 갈 수 있는 길을 담아서 도착지점에 갈때까지 연결한다.

from collections import deque
import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(N)]
distance = [[-1] * M for _ in range(N)]
distance[0][0] = 1


queue = deque()
queue.append((0, 0))

while queue:
    i, j = queue.popleft()


    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]
        if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and distance[ni][nj] == -1:
            queue.append((ni, nj))
            distance[ni][nj] = distance[i][j] + 1
            if ni == N - 1 and nj == M - 1:
                print(distance[ni][nj])
                sys.exit()
# print(distance[N-1][M-1])
# for line in distance:
#     print(*line)