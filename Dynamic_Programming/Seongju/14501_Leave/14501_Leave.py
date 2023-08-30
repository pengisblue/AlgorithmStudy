# 14501 - 퇴사
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
DP = [0] * (N + 2)
T = [0] * (N + 1)   # 상담 일수
P = [0] * (N + 1)   # 상담 수익

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

for j in range(N, 0, -1):
    if j + T[j] > N + 1:
        DP[j] = DP[j + 1]
    else:
        DP[j] = max(DP[j+1], DP[j + T[j]] + P[j])

print(DP[1])


