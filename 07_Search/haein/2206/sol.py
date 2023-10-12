from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

mi = [-1, 1, 0, 0]
mj = [0, 0, -1, 1]


def bfs():
    que = deque([(0, 0, False, 1)])
    visited1[0][0] = 1
    while que:
        ni, nj, wall, cnt = que.popleft()
        if ni == N-1 and nj == M-1:
            return cnt
        for idx in range(4):
            di = ni + mi[idx]
            dj = nj + mj[idx]
            if 0 <= di < N and 0 <= dj < M:
                if di == N-1 and dj == M-1:
                    return cnt + 1
                if not wall and not visited1[di][dj]:
                    visited1[di][dj] = 1
                    if graph[di][dj] == '0':
                        que.append((di, dj, wall, cnt+1))
                    elif graph[di][dj] == '1':
                        que.append((di, dj, True, cnt+1))
                if wall and not visited1[di][dj] and not visited2[di][dj]:
                    if graph[di][dj] == '0':
                        visited2[di][dj] = 1
                        que.append((di, dj, wall, cnt + 1))
    return -1


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited1 = [[0]*M for _ in range(N)]
visited2 = [[0]*M for _ in range(N)]
print(bfs())
