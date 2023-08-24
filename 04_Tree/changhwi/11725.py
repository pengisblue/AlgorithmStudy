n = int(input())

parent = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)
def dfs(start):
    for i in graph[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i)
dfs(1)
#print(parent)
for j in range(2, n+1):
    print(parent[j])

