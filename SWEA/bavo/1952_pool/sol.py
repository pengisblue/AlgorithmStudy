T = int(input())

for tc in range(T):
    day, month, quarter_month, year = map(int, input().split())
    plan = list(map(int, input().split()))

    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = min(plan[i - 1] * day, month) + dp[i - 1]
        if i > 2:
            dp[i] = min(dp[i - 3] + quarter_month, dp[i])
    # print(dp)
    print(f'#{tc + 1} {min(dp[12], year)}')