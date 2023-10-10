from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def move(locate, n):
    if n == 0:
        locate -= 1
    elif n == 1:
        locate += 1
    else:
        locate *= 2
    return locate


N, K = map(int, input().split())
queue = deque()
visited = [0] * 100001
queue.append(N)
visited[N] = 1
while queue:
    now = queue.popleft()
    for i in range(3):
        next_lo = move(now, i)
        if 0 <= next_lo <= 100000 and visited[next_lo] == 0:
            visited[next_lo] = visited[now] + 1
            if next_lo == K:
                break
            else:
                queue.append(next_lo)
    if visited[K]:
        print(visited[K]-1)
        break
