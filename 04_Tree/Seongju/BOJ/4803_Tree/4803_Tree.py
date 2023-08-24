# 4803 - 트리
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def DFS(node, p) :
    visited[node] = True

    for j in graph[node]:
        if j == p:
            continue
        if visited[j]:
            return False
        if not DFS(j, node):
            return False
    return True

answer = 0
cnt = 0
while True:
    n, m = map(int, input().split())
    cnt += 1
    answer = 0
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        if visited[i]:
            continue
        if DFS(i, 0) :
            answer += 1

    if answer == 0:
        print(f'Case {cnt}: No trees.')
    elif answer == 1:
        print(f'Case {cnt}: There is one tree.')
    else:
        print(f'Case {cnt}: A forest of {answer} trees.')


