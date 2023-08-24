import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(idx, val):
    global max_val, max_idx
    if max_val < val:
        max_val = val
        max_idx = idx

    # print(idx)

    for t in tree[idx]:
        next_idx, weight = t
        # print(t)
        if not visited[next_idx]:
            visited[next_idx] = True
            dfs(next_idx, val + weight)
            visited[next_idx] = False


N = int(input())

tree = [list() for _ in range(N + 1)]

for _ in range(N - 1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))
# print(tree)
visited = [False] * (N + 1)

max_val = 0
max_idx = 1

# 원점 기준으로 가중치가 제일 높은 동선 탐색
visited[1] = True
dfs(1, 0)
# 가중치가 가장 높았던 인덱스 기준으로 다시 dfs 탐색
# (원점이 아닌 다른 방향으로 순회하는 경우 점수가 더 높아질 수 있음)
visited = [False] * (N + 1)
visited[max_idx] = True
dfs(max_idx, 0)

print(max_val)
