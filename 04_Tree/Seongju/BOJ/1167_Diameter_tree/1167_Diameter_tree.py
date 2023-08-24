# 1167 - 트리의 지름
import sys
sys.stdin= open('input.txt')
sys.setrecursionlimit(10**9)

def DFS(node, val):
    for i in graph[node]:
        a, b = i
        if distance[a] == -1:
            distance[a] = val + b
            DFS(a, val + b)

V = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    w = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(w) - 2, 2):
        graph[w[0]].append([w[j], w[j + 1]])

distance = [-1] * (V+1)
distance[1] = 0
DFS(1, 0)

l = distance.index(max(distance))   # 가중치가 가장 높은 노드에서 다시 탐색
distance = [-1] * (V+1)
distance[l] = 0
DFS(l, 0)

print(max(distance))