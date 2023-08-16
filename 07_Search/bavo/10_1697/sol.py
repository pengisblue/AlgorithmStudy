from collections import deque

N, K = map(int, input().split())

queue = deque()

queue.append(N)

visited = [0] * 100_001

visited[N] = 1
while True:
    curr_loc = queue.popleft()
    x, y, z = curr_loc + 1, curr_loc - 1, curr_loc * 2

    if 0 <= x <= 100_000 and not visited[x]:
        visited[x] = visited[curr_loc] + 1
        queue.append(x)
    if 0 <= y <= 100_000 and not visited[y]:
        queue.append(y)
        visited[y] = visited[curr_loc] + 1
    if 0 <= z <= 100_000 and not visited[z]:
        queue.append(z)
        visited[z] = visited[curr_loc] + 1

    if x == K or y == K or z == K:
        break

print(visited[K] - 1)