from collections import deque
import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(input().rstrip()) for i in range(N)]
visited = [[0]*M for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
queue = deque()
queue.append([0, 0])
visited[0][0] = 1
goal = False
while queue:
    now = queue.popleft()
    for idx in range(4):
        row = now[0] + di[idx]
        col = now[1] + dj[idx]
        if 0 <= row < N and 0 <= col < M:
            if maze[row][col] == '1' and visited[row][col] == 0:
                # 길을 찾으면 이전 visited + 1 값을 visited에 할당하여 이동 횟수 체크
                visited[row][col] = visited[now[0]][now[1]] + 1
                if row == N-1 and col == M-1:
                    goal = True
                    break
                else:
                    queue.append([row, col])

    if goal:
        break
print(visited[N-1][M-1])
