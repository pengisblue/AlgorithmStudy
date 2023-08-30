# 2579 - 계단 오르기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input()) # 계단 개수
stairs = [int(input()) for _ in range(N)] # 계단 리스트
DP = [0] * N # dp 리스트

if len(stairs) <= 2:
    print(sum(stairs))
else: # 계단이 3개 이상일 때
    DP[0] = stairs[0] # 첫째 계단 수동 계산
    DP[1] = stairs[0] + stairs[1] # 둘째 계단까지 수동 계산
    for i in range(2, N): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        DP[i] = max(DP[i - 3] + stairs[i-1] + stairs[i], DP[i - 2] + stairs[i])

    print(DP[-1])

