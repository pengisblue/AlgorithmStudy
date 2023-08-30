import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    day_price, month_price, quarter_price, year_price = map(int, input().split())
    plan = list(map(int, input().split()))
    price = [plan[i] * day_price for i in range(12)]
    prefix_sum = [0] * 12
    for i in range(12):
        if price[i] > month_price:
            price[i] = month_price

    for i in range(12):
        if i == 0:
            prefix_sum[i] = min(price[i], quarter_price)
        else:
            sum_price = prefix_sum[i-1] + price[i]
            if i < 3:
                prefix_sum[i] = min(sum_price, quarter_price)
            else:
                new_price = prefix_sum[i-3] + quarter_price
                prefix_sum[i] = min(sum_price, new_price)

    print(f'#{tc}', min(prefix_sum[11], year_price))
