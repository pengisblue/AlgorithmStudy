# 이진탐색트리

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
# print = sys.stdout.write

def solution(node):
    if node.left is not None:
        solution(node.left)
    if node.right is not None:
        solution(node.right)
    print(node.val)


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


head_node = Node(int(input()))
curr_node = head_node
stack = []

while True:
    try:
        new_node = int(input())
        if new_node < curr_node.val:
            curr_node.left = Node(new_node)
            stack.append(curr_node)
            curr_node = curr_node.left

        else:
            while stack and new_node > stack[-1].val:
                curr_node = stack.pop()
            curr_node.right = Node(new_node)
            curr_node = curr_node.right
    except:
        break

# print(stack)
solution(head_node)