# 풍선 터뜨리기
import sys

input = sys.stdin.readline
N = int(input())
paper = [0] + list(map(int, input().split())) # 종이에 적힌 리스트
balloon = [0]*N # 풍선 리스트
idx = 0
answer = []

for i in range(N) :
    balloon[i] = i+1

while balloon :
    a = balloon.pop(idx)
    answer.append(a)
    if balloon :
        if paper[a] >
        idx = (idx + paper[a] - 1) % len(balloon)

print(*answer)