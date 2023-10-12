import sys
sys.stdin = open('input.txt')


def n_m(m, nums):
    if len(nums) == m:
        print(*nums)
    else:
        for i in range(1, N+1):
            n_m(m, nums+[i])


N, M = map(int, input().split())
n_m(M, [])
