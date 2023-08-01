import sys
sys.stdin = open('input.txt')

for T in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    total = 0
    for i in range(2, N - 2):
        x = max(buildings[i - 1], buildings[i - 2], buildings[i + 1], buildings[i + 2])
        if buildings[i] > x:
            total += buildings[i] - x
    print(f'#{T} {total}')