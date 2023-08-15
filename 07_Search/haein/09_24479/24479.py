import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(R):
    global cnt
    stack = [R]
    visited = [0] * (N + 1)
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            cnt += 1
            order[v-1] = cnt
            for link in graph[v]:
                if visited[link] == 0:
                    stack.append(link)

'''
RecursionError
def dfs(R):
    global cnt
    visited[R] = 1
    order[R-1] = cnt    # R의 방문 순서를 인덱스 R-1에 할당
    for link in graph[R]:   # R과 연결된 정점을 순회
        if visited[link] == 0:  # 방문하지 않았으면
            cnt += 1
            dfs(link)
'''

N, M, R = map(int, input().split())     # 정점, 간선, 시작
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
list(map(lambda x: x.sort(reverse=True), graph))
# graph = [[], [4, 2], [4, 3, 1], [4, 2], [3, 2, 1], []]
order = [0] * N      # 방문 순서를 담을 리스트
cnt = 0
dfs(R)

for i in order:
    print(i)
