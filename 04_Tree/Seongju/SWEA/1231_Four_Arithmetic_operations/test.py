import sys
sys.stdin = open('input.txt')

def Postorder(node):
    if node:
        Postorder(left[node]) # left
        Postorder(right[node]) # right
        print(v[node], end=' ')

T = 10
for t in range(1, T+1):
    N = int(input())
    v = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N):
        node_info = input().split()
        v[int(node_info[0])] = node_info[1]
        if len(node_info) == 4 :
            left[i+1] = int(node_info[2])
            right[i+1] = int(node_info[3])
    print(left)
    print(right)
    print(v)

    print(f'#{t}', end=' ')
    Postorder(1)
    print()