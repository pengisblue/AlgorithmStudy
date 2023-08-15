# 1012 - 유기농 배추
import sys
sys.stdin = open('input.txt')

def DFS(x, y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                DFS(nx, ny)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(sys.stdin.readline())
for t in range(1, T+1) :
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*N for _ in range(M)]
    cnt = 0

    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                DFS(a, b)
                cnt += 1

    print(cnt)