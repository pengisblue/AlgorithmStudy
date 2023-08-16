# 1260 - DFS & BFS
import sys
from collections import deque
sys.stdin = open('input.txt')

N, M, start = map(int, sys.stdin.readline().split())
A = [[] for _ in range(N+1)]

for m in range(M) :
    s, e = map(int, sys.stdin.readline().split())
    A[s].append(e)
    A[e].append(s)

for n in range(N+1):
    A[n].sort()

def DFS(node) :
    print(node, end=' ')
    visited[node] = True

    for i in A[node] :
        if not visited[i] :
            DFS(i)

visited = [False] * (N+1)
DFS(start)
print()

def BFS(node) :
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue :
        current = queue.popleft()
        print(current, end=' ')

        for j in A[current] :
            if not visited[j] :
                visited[j] = True
                queue.append(j)

visited = [False] * (N+1)
BFS(start)