import sys

sys.stdin = open('sample_input.txt')

T = int(sys.stdin.readline())

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())  # N = 정수의 갯수, M = 구간의 갯수
    Ai = list(map(int, sys.stdin.readline().split()))

    prefix_sum = []  # 구간 합
    answer = 0
    max_p = 0  # max 값 초기화
    min_p = float('inf')  # min 값 초기화
    sum_n = 0
    sum_list = [0] * (N + 1)

    for i in range(N):
        sum_n += Ai[i]
        sum_list[i + 1] = sum_n

    for j in range(N - M + 1):
        prefix_sum.append(sum_list[j + M] - sum_list[j])

    for k in prefix_sum:
        if k > max_p:
            max_p = k

        if k < min_p:
            min_p = k

    answer = max_p - min_p

    print(f'#{t + 1} {answer}')
