import sys

sys.setrecursionlimit(100_000)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(x, y):
    cabbage[x][y] = 0

    for k in range(4):
        ni, nj = x + dx[k], y + dy[k]
        if 0 <= ni < n and 0 <= nj < m and cabbage[ni][nj] == 1:
            dfs(ni, nj)


for _ in range(int(input())):
    m, n, k = map(int, input().split())

    cabbage = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        cabbage[j][i] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)
