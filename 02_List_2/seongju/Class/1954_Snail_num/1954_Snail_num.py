# 1954 - 달팽이 숫자
import sys
sys.stdin = open('input.txt')

T = int(input())

#  0->우, 1->하, 2->좌, 3->상
r_ls = [0, 1, 0, -1]    # 행 리스트
c_ls = [1, 0, -1, 0]    # 열 리스트

for t in range(1, T+1) :
    N = int(input())
    snail_list = [[0]*N for _ in range(N)]
    r, c = 0, 0
    d = 0 # 방향 -> 우

    for i in range(1, N*N + 1) :
        snail_list[r][c] = i
        r += r_ls[d]
        c += c_ls[d]

        if r < 0 or c < 0 or r >= N or c >= N or snail_list[r][c] != 0 :
            r -= r_ls[d]    # 이전 상태로 돌리기
            c -= c_ls[d]
            d = (d + 1) % 4     # 방향 전환
            r += r_ls[d]    # 방향 전환 후 이동
            c += c_ls[d]


    print(f'#{t}')
    for s in snail_list :
        print(*s)