# 알고리즘 수업 - 깊이 우선 탐색 1

import sys

input = sys.stdin.readline
sys.setrecursionlimit(200_000)
print = sys.stdout.write


def dfs(e, r):
    global depth
    visited[r] = True
    result[r - 1] = depth
    e[r].sort()

    depth += 1
    for i in e[r]:
        if not visited[i]:
            dfs(e, i)


n, m, start = map(int, input().split())

node_dict = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    node_dict[u].append(v)
    node_dict[v].append(u)

visited = [False] * (n + 1)
result = [0] * n

depth = 1

dfs(node_dict, start)

for i in result:
    print(str(i) + '\n')
