from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())    # 체스판 한 변의 길이
    now = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    di = [0, -2, -1, 1, 2, 2, 1, -1, -2]
    dj = [0, 1, 2, 2, 1, -1, -2, -2, -1]
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    queue.append(now)
    finish = False
    while queue:
        locate = queue.popleft()
        for i in range(9):
            dx = locate[0] + di[i]
            dy = locate[1] + dj[i]
            if 0 <= dx < N and 0 <= dy < N:
                if visited[dx][dy] == 0:
                    visited[dx][dy] = visited[locate[0]][locate[1]] + 1
                    if [dx, dy] == goal:
                        finish = True
                        break
                    else:
                        queue.append([dx, dy])

        if finish:
            print(visited[goal[0]][goal[1]] - 1)
            break
