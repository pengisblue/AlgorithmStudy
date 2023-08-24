from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited = [0] * (V+1)
    while queue:
        now = queue.popleft()
        for (i, distance) in graph[now]:
            if i != start and visited[i] == 0:
                visited[i] = visited[now] + distance
                queue.append(i)
    result = max(visited)
    num = visited.index(result)
    return num, result


V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    edge = list(map(int, input().split()))
    i = 1
    while edge[i] != -1:
        graph[edge[0]].append((edge[i], edge[i+1]))
        i += 2
# [[], [(3, 2)], [(4, 4)], [(1, 2), (4, 3)], [(2, 4), (3, 3), (5, 6)], [(4, 6)]]

print(bfs(bfs(1)[0])[1])
