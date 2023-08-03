import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N = int(input())
    numbers = sorted(list(map(int, input().split())))
    print(f"#{T + 1} {' '.join([str(numbers[(i // 2) + ((i + 1) % 2) * (N - 1 - i)]) for i in range(10)])}")


#   6
# 1 2 3 4 5 6 7 8 9 10 11
