import sys

input = sys.stdin.readline


def dfs(r):
    global cnt
    visited[r - 1] = True

    for i in connection[r]:
        if not visited[i - 1]:
            cnt += 1
            dfs(i)


n = int(input())
m = int(input())

connection = [[] for _ in range(n + 1)]

visited = [False] * n

cnt = 0

for i in range(m):
    x, y = map(int, input().split())
    connection[x].append(y)
    connection[y].append(x)

dfs(1)
print(cnt)
