import sys
input = sys.stdin.readline

N, M = map(int,input().split())

numbers = [[0 for col in range(N + 1)] for row in range(N + 1)]

for i in range(N):
    input_list = list(map(int,input().split()))
    for j in range(N):
        numbers[i + 1][j + 1] = input_list[j] + numbers[i][j + 1] + numbers[i + 1][j] - numbers[i][j]

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
        # prefix_sum[i][j] = numbers[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    result = numbers[x2][y2] - numbers[x2][y1 - 1] - numbers[x1 - 1][y2] + numbers[x1 - 1][y1 - 1]
    print(result)
