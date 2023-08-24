# 5174 - subtree
import sys

sys.stdin = open('input.txt')


def preorder(root):
    global cnt
    if root != 0:
        # print(root, end='')
        preorder(node_l[root])  # left
        preorder(node_r[root])  # right
        cnt += 1

    return cnt


T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())  # E = 간선 수, N = 루트
    fair = list(map(int, input().split()))  # 입력 받기
    node_l = [0] * (E + 2)  # 왼쪽 자식 노드
    node_r = [0] * (E + 2)  # 오른쪽 자식 노드
    cnt = 0  # 서브트리에 속한 노드의 개수 기록

    for i in range(0, E * 2 - 1, 2):
        if not node_l[fair[i]]:  # 왼쪽 자식 노드
            node_l[fair[i]] = fair[i + 1]
        else:  # 오른쪽 자식 노드
            node_r[fair[i]] = fair[i + 1]

    print(f'#{t}', preorder(N))
