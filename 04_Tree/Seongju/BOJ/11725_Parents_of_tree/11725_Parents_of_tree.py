# 11725 - 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt')

def DFS(node, node_ls, visited):
    for next in node_ls[node]:
        if not visited[next]:
            visited[next] = node
            DFS(next, node_ls, visited)

N = int(input())
node_ls = [[] for _ in range(N + 1)]

for n in range(N - 1):
    v1, v2 = map(int, input().split())
    node_ls[v1].append(v2)
    node_ls[v2].append(v1)

visited = [0] * (N + 1)
DFS(1, node_ls, visited)

for i in range(2, N + 1):
    print(visited[i])
