import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(index):
    queue = deque()
    queue.append(index)
    while queue:
        next_index = queue.popleft()
        if next_index == 99:
            return 1

        visitied[next_index] = True

        while node[next_index]:

            queue.append(node[next_index].pop())
    return 0


for _ in range(1):
    T, m = map(int, input().split())
    visitied = [False] * 100
    node = [[] for _ in range(100)]

    link_str = list(map(int, input().split()))

    for i in range(len(link_str) // 2):
        x = link_str[i * 2]
        y = link_str[i * 2 + 1]
        node[x].append(y)

    print(f'#{T} {bfs(0)}')
