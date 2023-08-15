# 2606 - 바이러스
import sys
sys.stdin = open('input.txt')

def DFS(node) :
    global cnt
    visited[node] = True

    for next in CF[node] :
        if not visited[next] :
            DFS(next)
            cnt += 1

    return cnt

N = int(sys.stdin.readline())
F = int(sys.stdin.readline())
CF = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for f in range(F) :
    v1, v2 = map(int, sys.stdin.readline().split())
    CF[v1].append(v2)
    CF[v2].append(v1)

print(DFS(1))