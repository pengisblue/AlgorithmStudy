# 24416 - 피보나치 수1
import sys
sys.stdin = open('input.txt')

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global cnt2
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[n]

n = int(input())
cnt1 = fib(n)
cnt2 = 0
f = [0] * (n+1)
fibonacci(n)
print(cnt1, cnt2)
