from collections import deque
import sys
sys.stdin = open('input2.txt')


def bfs():
    que = deque([(1, 1)])
    visited[1] = 1
    while que:
        now, step = que.popleft()
        for i in range(1, 7):
            goto = now + i
            if moving[goto]:
                goto = moving[goto]
            if goto == 100:
                return step
            elif goto < 100 and not visited[goto]:
                visited[goto] = 1
                next_step = step + 1
                que.append((goto, next_step))


N, M = map(int, input().split())
moving = [0] * 101
for _ in range(N):
    x, y = map(int, input().split())
    moving[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    moving[u] = v

visited = [0] * 100
print(bfs())
