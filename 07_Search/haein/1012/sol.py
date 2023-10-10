from collections import deque
import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    plants = [list(map(int, input().split())) for _ in range(K)]     # 배추 좌표 [열, 행]
    visited = [0] * K
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    cnt = 0     # 배추흰지렁이 마리 수
    for idx, plant in enumerate(plants):
        if visited[idx] == 0:
            visited[idx] = 1
            queue = deque()
            queue.append(plant)
            while queue:
                locate = queue.popleft()
                for i in range(4):
                    dx = locate[0] + dj[i]      # 인접 열
                    dy = locate[1] + di[i]      # 인접 행
                    if 0 <= dx < M and 0 <= dy < N:
                        if [dx, dy] in plants and visited[plants.index([dx, dy])] == 0:
                            visited[plants.index([dx, dy])] = 1
                            queue.append([dx, dy])
            cnt += 1

    print(cnt)
