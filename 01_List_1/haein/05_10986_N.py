import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]  # 합 배열
temp = 0
cnt = 0  # 합이 M으로 나누어 떨어지는 (i,j)쌍의 개수

for i in range(N):
    temp += arr[i]
    prefix_sum.append(temp)

