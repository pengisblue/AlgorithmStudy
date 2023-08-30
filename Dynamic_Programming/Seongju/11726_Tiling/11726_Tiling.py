# 11726 - 2*N 타일 채우기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
DP = [0] * (1001)
mod = 10007
DP[1] = 1
DP[2] = 2

for i in range(3, N+1):
    DP[i] = (DP[i-1] +DP[i-2]) % mod

print(DP[N])