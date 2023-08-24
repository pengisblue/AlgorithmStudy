# 1231 - 중위 순회
import sys

sys.stdin = open('input.txt')


def Inorder(node):
    if node <= N:
        Inorder(node * 2)   # left
        print(alpha_ls[node], end='')
        Inorder(node * 2 + 1)   # right


T = 10
for t in range(1, T + 1):
    N = int(input())
    alpha_ls = [0] * (N + 1)
    for i in range(N):
        node_info = list(input().split())
        alpha_ls[i + 1] = node_info[1]

    print(f'#{t}', end=' ')
    Inorder(1)
    print()
