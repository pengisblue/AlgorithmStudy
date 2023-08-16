from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# def bfs(R):
#     queue = deque()
#     queue.append(R)
#     visited = [0] * (N + 1)
#     cnt = 0     # 방문 순서
#     while queue:
#         v = queue.popleft()
#         if visited[v] == 0:
#             visited[v] = 1
#             cnt += 1
#             order[v-1] = cnt
#         for i in graph[v]:
#             if visited[i] == 0:
#                 queue.append(i)


N, M, R = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for edge in graph:
    edge.sort()     # 오름차순 정렬

visited = [0] * (N + 1)
visited[R] = 1
queue = deque()
queue.append(R)
cnt = 1     # 방문 순서
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            visited[i] = cnt
            queue.append(i)

for i in visited[1:]:
    print(i)
