from collections import deque
import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]


def bfs():
    global total
    que = deque(tomato)
    while que:
        ni, nj, day = que.popleft()
        for idx in range(4):
            dx = ni + di[idx]
            dy = nj + dj[idx]
            if 0 <= dx < N and 0 <= dy < M and not box[dx][dy]:
                box[dx][dy] = 1
                que.append((dx, dy, day+1))
                if total < day + 1:
                    total = day + 1


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

tomato = []
total = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i, j, 0))

bfs()
for i in range(N):
    for j in range(M):
        if not box[i][j]:
            total = -1
            break

print(total)
