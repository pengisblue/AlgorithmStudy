# 5178 - 노드의 합
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    node = [0] * (N + 1)
    for m in range(M):
        a, n = map(int, input().split())
        node[a] = n
    print(node)

    for i in range(N, 0, -1) :
        if i // 2 > 0 :
            node[i // 2] += node[i] # 부모노드 = 자식노드의 합
            print(node)

    print(f'#{t}', node[L])