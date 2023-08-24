# 1967 - 트리의 지름
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)

def DFS(node, val):
    for i in graph[node]:
        v, w = i
        if distance[v] == -1:
            distance[v] = val + w
            DFS(v, val + w)

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    p, c, value = map(int, input().split())
    graph[p].append([c, value])
    graph[c].append([p, value])

distance = [-1] * (n+1)
distance[1] = 0
DFS(1, 0)

l = distance.index(max(distance))   # 가중치가 가장 높은 노드에서 다시 탐색
distance = [-1] * (n+1)
distance[l] = 0
DFS(l, 0)

print(max(distance))