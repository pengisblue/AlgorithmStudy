import sys
sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):

    paper = [[0] * 10 for row in range(10)]

    N = int(input())

    for _ in range(N):
        x1, y1, x2, y2, color = map(int,input().split())

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if paper[i][j] != color:
                    paper[i][j] += color

    count = 0
    for line in paper:
        for dot in line:
            if dot >= 3:
                count += 1

    print(f"#{T} {count}")

