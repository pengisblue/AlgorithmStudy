dp = []

for i in range(10):
    temp = []
    for j in range(0, i + 1):
        if j == 0 or j == i:
            temp.append(1)
        else:
            temp.append(dp[i - 1][j] + dp[i - 1][j - 1])
    dp.append(temp)

for T in range(1, int(input()) + 1):
    n = int(input())

    print(f'#{T}')
    for i in range(n):
        print(*dp[i])

