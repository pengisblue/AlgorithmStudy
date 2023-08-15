import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

T = int(input())

queue = deque()

for _ in range(T):

    N = int(input())

    chess_board = [[0] * N for _ in range(N)]

    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    if (start_x, start_y) == (end_x, end_y):
        print(0)
        continue

    chess_board[start_x][start_y] = 1

    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and chess_board[nx][ny] == 0:
                chess_board[nx][ny] = chess_board[x][y] + 1
                queue.append((nx, ny))
        if chess_board[end_x][end_y] > 0:
            print(chess_board[end_x][end_y] - 1)
            break

    queue.clear()
