from collections import deque
import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    global total
    que = deque(tomato)
    while que:
        ni, nj, nk, day = que.popleft()
        for idx in range(6):
            di = ni + dx[idx]
            dj = nj + dy[idx]
            dk = nk + dz[idx]
            if 0 <= di < N and 0 <= dj < M and 0 <= dk < H and not box[dk][di][dj]:
                box[dk][di][dj] = 1
                que.append((di, dj, dk, day+1))
                if total < day+1:
                    total = day+1


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
tomato = []
total = 0
for i in range(N):
    for j in range(M):
        for k in range(H):
            if box[k][i][j] == 1:
                tomato.append((i, j, k, 0))

bfs()

for i in range(N):
    for j in range(M):
        for k in range(H):
            if not box[k][i][j]:
                total = -1
                break

print(total)
