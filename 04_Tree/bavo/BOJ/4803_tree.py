# 트리 유효성 검사

import sys

input = sys.stdin.readline


def dfs(idx, parent):
    global cycle
    visited[idx] = True

    for next_idx in connection[idx]:
        if not visited[next_idx]:
            dfs(next_idx, idx)
        else:
            if parent != next_idx:
                cycle = True


case = 1

while True:
    N, M = map(int, input().split())

    if (N, M) == (0, 0):
        break

    connection = [list() for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        connection[x].append(y)
        connection[y].append(x)

    tree_cnt = 0
    visited = [0] * (N + 1)

    for i in range(1, N + 1):
        if not visited[i]:
            cycle = False
            dfs(i, -1)
            if not cycle:
                tree_cnt += 1

    if tree_cnt == 0:
        print(f'Case {case}: No trees.')
    elif tree_cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {tree_cnt} trees.')

    case += 1
