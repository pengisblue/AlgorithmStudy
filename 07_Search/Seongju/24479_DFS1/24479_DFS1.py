# 24479 - DFS1
import sys
sys.setrecursionlimit(150000)
sys.stdin = open('input.txt')

def DFS(R) : #R = 시작 정점
    global cnt
    visited[R] += cnt   # 방문 순서 표시
    graph[R].sort()
    for next in graph[R]:
        if visited[next] == 0 :
            cnt += 1
            DFS(next)

    return visited

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N+1)
cnt = 1

for m in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(R)

for i in range(1, N + 1):
    print(visited[i])