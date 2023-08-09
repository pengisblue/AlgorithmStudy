import heapq
import sys
sys.stdin = open('input.txt')

def inorder(node):
    global cnt
    if node <= N:
        inorder(node*2)
        tree[node] = cnt
        cnt += 1
        inorder(node*2+1)

T = int(input())
for t in range(T):
    N = int(input())
    tree = [0] * 
    num_list = list(map(int, input().split()))
    heapq.heapify(num_list)
