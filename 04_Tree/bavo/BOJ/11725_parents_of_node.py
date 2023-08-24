import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(idx):
    for next_node in edge[idx]:
        if not visited[next_node]:
            visited[next_node] = idx
            dfs(next_node)


N = int(input())

edge = [list() for _ in range(N + 1)]

for _ in range(N - 1):
    x, y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)

visited = [0] * (N + 1)
dfs(1)
print('\n'.join(list(map(str, visited[2:]))))
