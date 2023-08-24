import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open('input.txt')

def pre_order(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return
    root = post_order[post_r]
    mid = node_num[root]

    left = mid - in_l
    right = in_r - mid

    print(root, end=' ')
    pre_order(in_l, in_l + left -1, post_l, post_l + left - 1)  # left
    pre_order(in_r - right + 1, in_r, post_r - right, post_r - 1)  # right

n = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))     # 중위 순회
post_order = list(map(int, sys.stdin.readline().split()))   # 후위 준회

node_num = [0] * (n + 1)
for i in range(n):
    node_num[in_order[i]] = i

pre_order(0, n-1, 0, n-1)