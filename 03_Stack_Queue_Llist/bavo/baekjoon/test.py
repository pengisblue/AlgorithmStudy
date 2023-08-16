from collections import deque


def bfs(N, start):
    cnt = 1
    visited = [0] * (N + 1)
    que = deque([start])
    visited[start] = cnt
    cnt += 1
    while que:
        now = que.popleft()
        for i in node[now]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = cnt
                cnt += 1
    return visited[1:]


N, M, R = map(int, input().split())
node = [[] for _ in range(N + 1)]
for _ in range(N):
    start, end = map(int, input().split())
    node[start].append(end)
    node[end].append(start)
for i in range(1, N + 1):
    node[i].sort(reverse=True)
print(*bfs(N, R), sep='\n')