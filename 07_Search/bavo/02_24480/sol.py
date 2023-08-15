# 알고리즘 수업 - 깊이 우선 탐색 2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(200_000)

def dfs(start):
    global depth
    visitied[start] = depth
    node[start].sort(reverse=True)

    for i in node[start]:
        if not visitied[i]:
            depth += 1
            dfs(i)


n, m, r = map(int, input().split())

node = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

depth = 1
visitied = [0] * (n + 1)

dfs(r)
for i in range(1, n + 1):
    print(visitied[i])
