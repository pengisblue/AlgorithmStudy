import sys
sys.stdin = open('input.txt')

for T in range(10):
    int(input())
    a = [list(map(int,input().split())) for _ in range(100)]
    print(f'#{T+1} {max( max([sum(b) for b in list(zip(*a))]), max([sum(b) for b in a]), sum(a[i][i] for i in range(100)), sum(a[i][99-i] for i in range(100)) )}')

    # max([sum(b) for b in list(zip(*a))])   열 합의 max
    # max([sum(b) for b in a])               행 합의 max
    # sum(a[i][i] for i in range(100))       대각선 합(좌 -> 우)
    # sum(a[i][99-i] for i in range(100)) )  대각선 합(우 -> 좌)
