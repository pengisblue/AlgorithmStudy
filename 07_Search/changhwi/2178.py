from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
graph = []
for i in range(N):
  graph.append(list(map(int, input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  que = deque()
  que.append((x,y))

  while que:
    x,y = que.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if nx<0 or ny<0 or nx>=N or ny >= M:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        que.append((nx, ny))
  return graph[N-1][M-1]

print(bfs(0,0))