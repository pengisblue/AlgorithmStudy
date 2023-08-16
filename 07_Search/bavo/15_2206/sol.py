import sys

input = sys.stdin.readline

from collections import deque


def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def bfs(start, end):
    visited = set()
    queue = deque([(start[0], start[1], 1, 0)])  # (x, y, steps, walls_broken)

    while queue:
        x, y, steps, walls_broken = queue.popleft()

        if (x, y) == end:
            return steps

        if (x, y, walls_broken) in visited:
            continue
        visited.add((x, y, walls_broken))

        index = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for nx, ny in index:
            if is_valid(nx, ny, N, M):
                if maze[nx][ny] == 0:
                    queue.append((nx, ny, steps + 1, walls_broken))
                elif walls_broken == 0:
                    queue.append((nx, ny, steps + 1, 1))
    return -1


N, M = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs((0, 0), (N - 1, M - 1)))
