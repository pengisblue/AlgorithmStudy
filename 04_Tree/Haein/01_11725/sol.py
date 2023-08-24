from collections import deque
import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline


def bfs():
    queue = deque([1])
    while queue:
        parent = queue.popleft()
        for child in graph[parent]:
            if tree[child] == 0:
                tree[child] = parent
                queue.append(child)


N = int(input())
tree = [0] * (N+1)      # 부모를 저장할 리스트
tree[1] = 1
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()
for i in range(2, N+1):
    print(tree[i])
