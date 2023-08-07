import sys
sys.stdin = open('input.txt')

N = 10  # 케이스 개수
M = 99  # 마지막 줄 행의 값

for n in range(1, N + 1):
    T = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]

    # x 위치 구하기
    x = 2  # x 값
    x_idx = ladder_list[M].index(2)  # x의 열 위치

    cur_c = M  # 현재 위치 행
    cur_r = x_idx  # 현재 위치 열
    up_count = 0  # 위로 올라간 횟수

    # 더 이상 이동할 곳이 없을 때까지 while 문
    while up_count < M:  # 위로 이동한 횟수가 99가 될때까지!
        cur_c -= 1
        up_count += 1
        ladder_list[cur_c + 1][cur_r] = '*'

        # if 좌우 체크
        if 0 <= cur_r - 1 < 100:
            if ladder_list[cur_c][cur_r - 1] == 1:  # 좌측 이동
                while (cur_r - 1 >= 0) and (ladder_list[cur_c][cur_r - 1] == 1):  # 현재위치에서 좌측 값이 1일 때만
                    cur_r -= 1
                    ladder_list[cur_c][cur_r + 1] = '*'

        if 0 <= cur_r + 1 < 100:
            if ladder_list[cur_c][cur_r + 1] == 1:  # 우측 이동
                while (cur_r + 1 < 100) and (ladder_list[cur_c][cur_r + 1] == 1):  # 현재위치에서 우측 값이 1일 때만
                    cur_r += 1
                    ladder_list[cur_c][cur_r - 1] = '*'

    print(f'#{n} {cur_r}')