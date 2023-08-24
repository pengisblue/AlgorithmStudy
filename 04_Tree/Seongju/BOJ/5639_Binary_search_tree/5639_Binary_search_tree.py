# 5639 - 이진 검색 트리
import sys

sys.setrecursionlimit(10 ** 9)
sys.stdin = open('input.txt')

def Post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if node[i] > node[start]:
            mid = i
            break

    Post(start + 1, mid - 1)  # left
    Post(mid, end)  # right
    print(node[start])

node = []
while True:
    try:
        node.append(int(input()))
    except EOFError:
        break

Post(0, len(node) - 1)
