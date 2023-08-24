import sys

input = sys.stdin.readline


def dfs(idx, val):
    global max_val, max_index

    if max_val < val:
        max_val = val
        max_index = idx

    for t in tree[idx]:
        next_node, weight = t
        # print(t)
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, weight + val)
            visited[next_node] = False


N = int(input())

tree = [list() for _ in range(N + 1)]

root_index = 0
root_len = 0
for _ in range(N):
    node, *edge, end = map(int, input().split())
    for i in range(len(edge) // 2):
        tree[node].append((edge[i * 2], edge[i * 2 + 1]))

    if len(edge) > root_len:
        root_len = len(edge)
        root_index = node

max_val = 0
max_index = 0
visited = [False] * (N + 1)
visited[root_index] = True
dfs(root_index, 0)
visited = [False] * (N + 1)
visited[max_index] = True
dfs(max_index, 0)

print(max_val)
