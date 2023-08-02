import sys

sys.stdin = open('input.txt')

T = int(input())

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for t in range(1, T+1) :
    N, K = map(int, input().split())
    # N = 부분집합의 원소의 개수, K = 부분집합의 원소의 합
    num = len(numbers)  # 집합의 원소의 개수
    cnt = 0    # 정답 값의 개수 변수 선언

    for x in range(1 << num):
        subset = []

        for y in range(num):    # 부분집합 구하기
            if x & (1 << y):
                subset.append(numbers[y])

        if len(subset) == N :   # 부분집합의 개수가 N인 경우
            sum_s = 0   # 부분집합들의 합 변수 선언
            for i in range(len(subset)) :   # 부분집합들의 합 구하기
                sum_s += subset[i]
            if sum_s == K : # 부분집합들의 합이 K인 경우
                cnt += 1

    print(f'#{t} {cnt}')
