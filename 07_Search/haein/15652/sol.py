import sys
sys.stdin = open('input.txt')


def n_m(n, nums):
    if len(nums) == M:
        print(*nums)

    else:
        for i in range(1, N+1):
            if n <= i:
                n_m(i, nums+[i])


N, M = map(int, input().split())
n_m(1, [])
