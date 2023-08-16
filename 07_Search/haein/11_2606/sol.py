from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

V = int(input())
M = int(input())
graph = [[] for i in range(V+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
visited = [0] * (V+1)
queue.append(1)
visited[1] = 1
while queue:
    v = queue.popleft()
    for link in graph[v]:
        if visited[link] == 0:
            visited[link] = 1
            queue.append(link)
result = sum(visited) - 1   # 1번을 제외한 방문 정점의 개수
print(result)
