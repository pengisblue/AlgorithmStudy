# 2667 - 단지번호 붙이기
import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS(graph, r, c) :
    queue = deque()
    queue.append((r, c))
    graph[r][c] = 0
    cnt_q = 1

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph) :
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt_q += 1
    return cnt_q

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = []
for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            cnt.append(BFS(graph, i, j))
            print(cnt)

cnt.sort()
print(len(cnt))
for i in range(len(cnt)) :
    print(cnt[i])