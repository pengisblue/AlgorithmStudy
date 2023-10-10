from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(r):
    queue = deque()
    queue.append(r)
    visited = [0] * (N+1)
    visited[r] = 1
    cnt = 1
    order[r-1] = cnt
    while queue:
        start = queue.popleft()
        for link in graph[start]:
            if visited[link] == 0:
                visited[link] = 1
                cnt += 1
                order[link-1] = cnt
                queue.append(link)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

list(map(lambda x: x.sort(reverse=True), graph))
order = [0] * N
bfs(R)
for i in order:
    print(i)
