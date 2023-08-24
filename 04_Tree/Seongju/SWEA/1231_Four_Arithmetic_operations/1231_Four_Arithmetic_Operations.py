# 1231 - 사칙연산
import sys
sys.stdin = open('input.txt')

def Postorder(node):
    if node:
        Postorder(left[node]) # left
        Postorder(right[node]) # right
        if v[node] == '+':
            v[node] = int(v[left[node]]) + int(v[right[node]])
        elif v[node] == '-':
            v[node] = int(v[left[node]]) - int(v[right[node]])
        elif v[node] == '*':
            v[node] = int(v[left[node]]) * int(v[right[node]])
        elif v[node] == '/':
            v[node] = int(v[left[node]]) // int(v[right[node]])


T = 10
for t in range(1, T+1):
    N = int(input())
    v = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(1, N+1):
        node_info = input().split()
        v[i] = node_info[1]
        if len(node_info) == 4 :
            left[i] = int(node_info[2])
            right[i] = int(node_info[3])

    Postorder(1)
    print(f'#{t}', v[1])