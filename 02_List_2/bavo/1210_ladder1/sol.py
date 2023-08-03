import sys


def turn(x, y):
    return (y < len(ladder) - 1 and ladder[x][y + 1])  == 1 or (y > 0 and ladder[x][y - 1]) == 1


def search(x, y):

    while x > 0:
        while (not turn(x, y)) and x > 0:
            # print(x, y)
            x -= 1

        if x == 0: break
        # print(x, y)

        if y < len(ladder) - 1 and ladder[x][y + 1] == 1:
            while y < len(ladder) - 1 and ladder[x][y + 1] == 1:
                y += 1
            x -= 1
        elif y > 0 and ladder[x][y - 1] == 1:
            while y > 0 and ladder[x][y - 1] == 1:
                y -= 1
            x -= 1
    return y


sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    start_x = len(ladder) - 1
    start_y = ladder[-1].index(2)

    print(f'#{T} {search(start_x, start_y)}')