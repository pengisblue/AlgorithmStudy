import sys

sys.stdin = open('input.txt')


# 펑션콜이 재귀메모리에 들어가면 재귀
# 그냥 리스트에 들어가면 스택

def dfs(index):
    global arrived

    if arrived:
        return

    visitied[index] = True
    # node[0] = [1, 2]
    # node[1] = [3, 4]
    # node[3] = [7]
    # node[7] = [99]
    for next in node[index]:
        if next == 99:
            arrived = True
            return
        if not visitied[next]:
            dfs(next)
            # stack


            # dfs(2)
            # dfs(3)
            # dfs(4)
            # dfs(7)


for _ in range(10):
    T, m = map(int, input().split())
    visitied = [False] * 100

    node = [[] for _ in range(100)]

    link_str = list(map(int, input().split()))
    # 1 2 | 3 4
    for i in range(len(link_str) // 2):
        x = link_str[i * 2]
        y = link_str[i * 2 + 1]
        node[x].append(y)

    arrived = False
    # 0 ~ 99
    dfs(0)
    print(f'#{T} {int(arrived)}')
