from collections import deque
import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline


def dfs(start):
    stack = deque()
    stack.append(start)
    visited = [0] * (N+1)
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            print(v, end=' ')
            for i in range(len(graph[v])-1, -1, -1):
                if visited[graph[v][i]] == 0:
                    stack.append(graph[v][i])


def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [0] * (N+1)
    visited[start] = 1
    print(start, end=' ')
    while queue:
        v = queue.popleft()
        for link in graph[v]:
            if visited[link] == 0:
                visited[link] = 1
                queue.append(link)
                print(link, end=' ')


N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

list(map(lambda x: x.sort(), graph))
dfs(V)
print()
bfs(V)
