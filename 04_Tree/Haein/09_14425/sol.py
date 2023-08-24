import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
S = {}
result = 0
for _ in range(N):
    S[input().rstrip()] = 1

for _ in range(M):
    result += S.get(input().rstrip(), 0)

print(result)
