# Average
import sys

N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))
M = 0
sum_test = 0
avg_test = 0

for i in T :
    if M < i :
        M = i

for j in range(N) :
    sum_test += (T[j] / M * 100)
    avg_test = sum_test / N

print(avg_test)