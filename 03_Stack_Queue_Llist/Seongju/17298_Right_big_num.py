# 오큰수  NGE(i)
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [0]*N

for i in range(N) :
    while stack and A[stack[-1]] < A[i] :
        answer[stack.pop()] = A[i]
    stack.append(i)

while stack :
    answer[stack.pop()] = -1

print(*answer)

