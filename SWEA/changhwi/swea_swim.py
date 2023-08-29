t = int(input())
for t in range(t):
    dp = [0] * 13
    money = list(map(int, input().split()))
    month = list(map(int, input().split()))
    month.insert(0, 0)  # 1월 부터 시작

    # 1월 부터 ~ x월까지 지불 금액 누적값 계산
    for i in range(13):
        # 하루가격 * 방문일수 > 한 달 가격 -> 이번 달 누적금 = 이전 달까지 누적금 + 한 달 가격
        if money[0] * month[i] > money[1]:
            dp[i] = dp[i - 1] + money[1]

        # 하루가격 * 방문일수 <= 한 달 가격 -> 이번 달 누적금 = 이전 달까지 누적 + 하루가격 * 방문일수
        else:
            dp[i] = dp[i - 1] + money[0] * month[i]

        # 3개월 이용권 가격이 (하루 or 한 달)로 결제한 가격보다 싸면
        # 현재값은 3개월 전 가격 + 3개월 이용권 가격
        if i > 2:
            if dp[i] > money[2] + dp[i - 3]:
                dp[i] = money[2] + dp[i - 3]

    # 12월까지 누적값보다 1년 이용권 가격이 싸면 1년치 한 번에 결제
    if dp[12] > money[3]:
        print(f'#{t + 1} {money[3]}')
    else:
        print(f'#{t + 1} {dp[12]}')

