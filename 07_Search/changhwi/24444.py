import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split()) 
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) 
c = 1 # 방문순서
def bfs(graph, start, visited):
    global c
    queue = deque([start])
    visited[start] = c 
    
    while queue:
        v = queue.popleft()
        for i in graph[v]: 
            if visited[i] == 0: 
                queue.append(i)
                c += 1 
                visited[i] = c

for i in range(m):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

for i in range(n+1): 
    graph[i].sort()
#print(graph)

bfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])