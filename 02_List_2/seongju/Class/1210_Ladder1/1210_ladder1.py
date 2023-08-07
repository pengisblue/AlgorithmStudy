import sys
sys.stdin = open('input.txt')

N = 10  # 케이스 개수

for n in range(1, N+1) :
    T = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]

    # x 위치 구하기
    x_idx = ladder_list[99].index(2)    # x의 열 위치

    cur_r = 99       # 현재 위치 행
    cur_c = x_idx   # 현재 위치 열
    up_cnt = 0    # 위로 올라간 횟수

    # 더 이상 이동할 곳이 없을 때까지 while 문
    while up_cnt < 99 : # 위로 이동한 횟수가 99가 될 때까지!
        cur_r -= 1
        up_cnt += 1

        # 좌우 체크
        while (0 <= cur_c - 1 and ladder_list[cur_r][cur_c - 1] == 1) or (cur_c + 1 < 100 and ladder_list[cur_r][cur_c + 1] == 1):
            if (0 <= cur_c - 1 and ladder_list[cur_r][cur_c - 1] == 1) :
                while (ladder_list[cur_r][cur_c - 1] == 1) : # 현재위치에서 좌측 값이 1일 때만
                    cur_c -= 1
                    if (cur_c - 1 < 0):
                        break
                break

            elif (cur_c + 1 < 100 and ladder_list[cur_r][cur_c + 1] == 1) :
                while (ladder_list[cur_r][cur_c + 1] == 1) : # 현재위치에서 우측 값이 1일 때만
                    cur_c += 1
                    if (cur_c + 1 >= 100):
                        break

                break

    print(f'#{n} {cur_c}')