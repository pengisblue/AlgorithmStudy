import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())

    numbers = []

    for i in range(100):
        numbers.append(list(map(int, input().split())))

    # 대각선 좌 -> 우
    diagonal_sum1 = 0
    # 대각선 우 -> 좌
    diagonal_sum2 = 0

    max_sum = 0

    for i in range(100):
        vertical_sum = 0
        horizontal_sum = 0
        for j in range(100):
            # 행 합 구하기
            horizontal_sum += numbers[i][j]
            # 열 합 구하기
            vertical_sum += numbers[j][i]

            # i와 j가 같을땐 대각선으로 가로지름
            if i == j:
                diagonal_sum1 += numbers[i][j]
                diagonal_sum2 += numbers[i][99 - j]
                # len(arr) - 1 - j
        # max_sum = max(max_sum, horizontal_sum)
        if horizontal_sum > max_sum:
            max_sum = horizontal_sum
        # max_sum = max(max_sum, vertical_sum)
        if vertical_sum > max_sum:
            max_sum = vertical_sum

    # max_sum = max(max_sum, diagonal_sum1)
    if diagonal_sum1 > max_sum:
        max_sum = diagonal_sum1
    # max_sum = max(max_sum, diagonal_sum2)
    if diagonal_sum2 > max_sum:
        max_sum = diagonal_sum2

    print(f'#{T} {max_sum}')