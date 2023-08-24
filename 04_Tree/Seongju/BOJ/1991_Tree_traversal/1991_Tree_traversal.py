# 트리 순회
import sys

sys.stdin = open('input.txt')


def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')
        inorder(tree[root][1])  # right


def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')


N = int(input())
tree = {}

for n in range(N):
    v, l, r = sys.stdin.readline().strip().split()
    tree[v] = [l, r]
print(tree)

preorder('A')
print()
inorder('A')
print()
postorder('A')
