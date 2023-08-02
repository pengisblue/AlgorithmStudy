# 1209 - Sum

import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, T+1) :
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    sum_arr = []
    max_n = 0

    # 각 행의 합
    for i in range(100):
        sum_c = 0
        for j in range(100) :
            sum_c += arr[i][j]
        sum_arr.append(sum_c)

    # 각 열의 합
    for j in range(100) :
        sum_r = 0
        for i in range(100) :
            sum_r += arr[i][j]
        sum_arr.append(sum_r)


    # 각 대각선의 합
    sum_d1 = 0
    sum_d2 = 0
    for k in range(100) :
        sum_d1 += arr[k][k]
        sum_d2 += arr[99-k][k]
    sum_arr.append(sum_d1)
    sum_arr.append(sum_d2)

    # max 값 구하기
    for m in sum_arr :
        if m > max_n :
            max_n = m

    print(f'#{t} {max_n}')