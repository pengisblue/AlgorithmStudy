V = int(input())
E = int(input())
graph = [[]*V for _ in range(V+1)]
for t in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)    
cnt = 0
visited = [0]*(V+1)
def dfs(node):
    global cnt
    visited[node] = 1
    #print(visited)
    for i in graph[node]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
 
dfs(1)
print(cnt)