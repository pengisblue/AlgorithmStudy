import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 크기, 횟수
numbers = [list(map(int, input().split())) for i in range(N)]
prefix_sums = [[0] * N]

for i in range(N):
    prefix_sum = [0]
    temp = 0
    for j in range(N):
        temp += numbers[i][j]
        prefix_sum.append(temp)
    prefix_sums.append(prefix_sum)

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for i in range(x1, x2+1):
        result = prefix_sums[i][y2] - prefix_sums[i][y1-1]
        ans += result
    print(ans)