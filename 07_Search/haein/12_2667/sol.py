from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
houses = [list(map(int, input().rstrip())) for _ in range(N)]   # input 받는 단지 위치
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
visited = [[0] * N for _ in range(N)]
cnt_complex = []    # cnt_house를 담아둘 리스트
for i in range(N):      
    for j in range(N):      # houses를 순회하면서 집이 있는지 확인한다
        cnt_house = 0       # 한 단지에 포함되는 집의 수
        queue = deque()     # bfs를 이용해서 탐색
        if houses[i][j] == 1 and visited[i][j] == 0:    # 집이 있고 방문한 적이 없다면
            visited[i][j] = 1       # 방문
            queue.append([i, j])    # 인접한 집을 탐색하기위해 좌표를 추가
            cnt_house += 1      # 집의 수 추가
            while queue:        # 인접한 집들을 모두 확인할 때 까지 반복
                locate = queue.popleft()
                for k in range(4):      # 인접 방향 탐색
                    dx, dy = locate[0]+di[k], locate[1]+dj[k]   # 탐색할 방향의 좌표를 새로운 변수에 할당
                    if 0 <= dx < N and 0 <= dy < N:     # 인덱스 범위 안에서
                        if houses[dx][dy] == 1 and visited[dx][dy] == 0:    # 집이 있고 방문한 적이 없다면
                            visited[dx][dy] = 1     # 방문
                            queue.append([dx, dy])  # 탐색목록에 좌표를 추가
                            cnt_house += 1      # 집의 수 추가
            cnt_complex.append(cnt_house)   # 탐색이 끝나면 집의 개수를 리스트에 추가

cnt_complex.sort()  # 정렬
print(len(cnt_complex))
for cnt in cnt_complex:
    print(cnt)
