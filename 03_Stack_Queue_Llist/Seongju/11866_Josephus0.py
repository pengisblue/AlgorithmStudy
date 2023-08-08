# 요세푸스 문제 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
circle = []
stack = []
idx = K - 1
for i in range(1, N+1) :    # 인덱스 0~N-1  값 1~N
    circle.append(i)

while circle :  # idx = 2 , circle[2] = 3
    stack.append(circle.pop(idx)) # pop후 circle[2] = 4
    if circle :
        idx = (idx + K -1) % len(circle)

print('<', end='')
print(*stack, sep=', ', end='')
print('>')

