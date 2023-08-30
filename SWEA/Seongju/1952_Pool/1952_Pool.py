import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    day, month_1, month_3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    min_sum = [0] * 13
    answer = 0

    for i in range(1, 13):
        min_sum[i] = min_sum[i - 1] + min(plan[i] * day, month_1)

        if i >= 3:
            min_sum[i] = min(min_sum[i], min_sum[i - 3] + month_3)

    answer = min(min_sum[12], year)
    print(f'#{t}', answer)
