# 24445 - BFS2
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
    A[n].sort(reverse=True)

def BFS(node) :
    global cnt
    queue = deque()
    queue.append(node)
    visited[node] = cnt

    while queue :
        current = queue.popleft()

        for j in A[current] :
            if not visited[j] :
                cnt += 1
                visited[j] = cnt
                queue.append(j)
    return visited

visited = [0] * (N+1)
cnt = 1
BFS(start)
for i in range(1, N + 1):
    print(visited[i])