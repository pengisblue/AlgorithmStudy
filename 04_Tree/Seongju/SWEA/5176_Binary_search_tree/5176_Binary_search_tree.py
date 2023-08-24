# 5176 - 이진탐색
import sys

sys.stdin = open('input.txt')


def Make_tree(n):
    global cnt
    if n <= N:
        Make_tree(n * 2)    # left
        tree[n] = cnt
        cnt += 1
        Make_tree(n * 2 + 1)    # right


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    E = N - 1  # 간선의 수
    tree = [0 for i in range(N + 1)]
    cnt = 1
    Make_tree(1)
    print(tree)

    print(f'#{t}', tree[1], tree[N // 2])
