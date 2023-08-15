import sys

sys.stdin = open('input.txt')


def dfs(index):
    stack = [index]

    while stack:
        next_index = stack.pop()
        if not visitied[next_index]:
            print(next_index, end=' ')
        if next_index == 99:
            return 1

        visitied[next_index] = True
        while node[next_index]:
            stack.append(node[next_index].pop())
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

    print(f'#{T} {dfs(0)}')
