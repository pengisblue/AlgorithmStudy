import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 개수, 합을 구하는 횟수
numbers = list(map(int, input().split()))
prefix_sum = [0]
sum_numbers = 0
for number in numbers:
    sum_numbers += number
    prefix_sum.append(sum_numbers)  # 합배열

for _ in range(M):
    i, j = map(int, input().split())  # 합을 구해야 하는 구간
    result = prefix_sum[j] - prefix_sum[i - 1]  # 구간 합
    print(result)
