import sys
input = sys.stdin.readline
sys.setrecursionlimit(100_000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global apart_cnt
    apartment[x][y] = 0
    apart_cnt += 1

    for k in range(4):
        ni, nj = x + dx[k], y + dy[k]
        if 0 <= ni < N and 0 <= nj < N and apartment[ni][nj] == 1:
            dfs(ni, nj)


N = int(input())

apartment = [list(map(int, input().rstrip())) for _ in range(N)]

apart_index = 0

result = []

for i in range(N):
    for j in range(N):
        if apartment[i][j] == 1:
            apart_index += 1
            apart_cnt = 0
            dfs(i, j)
            result.append(apart_cnt)

print(apart_index)

result.sort()
for num in result:
    print(num)
