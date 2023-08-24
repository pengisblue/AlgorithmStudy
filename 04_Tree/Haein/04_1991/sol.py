import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def preorder(node):
    if node != 0:
        print(chr(node+64), end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print(chr(node+64), end='')
        inorder(tree[node][1])


def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(chr(node+64), end='')


N = int(input())
tree = [[0]*3 for _ in range(N+1)]
for _ in range(N):
    node, left, right = input().split()
    if left != '.':
        tree[ord(node)-64][0] = ord(left) - 64
        tree[ord(left)-64][2] = ord(node) - 64
    if right != '.':
        tree[ord(node)-64][1] = ord(right) - 64
        tree[ord(right)-64][2] = ord(node) - 64

preorder(1)
print()
inorder(1)
print()
postorder(1)
