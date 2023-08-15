import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(R):
    global cnt
    stack = [R]
    visited = [0] * (N+1)
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            cnt += 1
            order[v-1] = cnt
            for link in graph[v]:
                if visited[link] == 0:
                    stack.append(link)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
list(map(lambda x: x.sort(), graph))
order = [0] * N
cnt = 0
dfs(R)
for i in order:
    print(i)
