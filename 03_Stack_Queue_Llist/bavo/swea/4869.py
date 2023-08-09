dp = [0, 1, 3, 5] + ([0] * 27)

for i in range(4, 31):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]

for T in range(int(input())):
    print(f'#{T+1} {dp[int(input()) // 10]}')

