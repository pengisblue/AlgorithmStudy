# 10844 - 쉬운 계단 수
import sys

sys.stdin = open('input.txt')

N = int(input())
DP = [[0] * 10 for _ in range(N+1)]
mod = 1000000000

for i in range(1, 10):
    DP[1][i] = 1

for j in range(2, N + 1):
    DP[j][0] = DP[j - 1][1]
    DP[j][9] = DP[j - 1][8]
    for k in range(1, 9):
        DP[j][k] = (DP[j - 1][k - 1] + DP[j - 1][k + 1]) % mod

sum_dp = 0
for M in range(10):
    sum_dp = (sum_dp + DP[N][M]) % mod

print(sum_dp)