import sys
sys.stdin = open('input.txt')


for T in range(1, int(input()) + 1):

    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    # 1 2 3 4 5 6 7 8 9 10
    # 3개 구간의 합
    # 1, 2, 3 sum  = 6
    #  6 + 4 10

    curr_val = 0

    for i in range(M):
        curr_val += numbers[i]

    max_val = min_val = curr_val

    for i in range(M, N):
        curr_val = curr_val + numbers[i] - numbers[i - M]

        if max_val < curr_val:
            max_val = curr_val

        if min_val > curr_val:
            min_val = curr_val

    print(f'#{T} {max_val - min_val}')