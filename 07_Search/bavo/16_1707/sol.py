from collections import deque
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


t = int(input())
for T in range(t):

    V, E = map(int, input().split())

    apex = [0] * (V + 1)

    line = [list() for _ in range(V + 1)]

    for _ in range(E):
        x, y = map(int, input().split())
        line[x].append(y)
        line[y].append(x)

    queue = deque()

    end = False

    for i in range(1, V + 1):
        if apex[i] == 0:
            queue.append(i)
            apex[i] = 1
            while queue:
                curr = queue.pop()
                for next in line[curr]:
                    if apex[next] == 0:
                        if apex[curr] == 1:
                            apex[next] = 2
                        elif apex[curr] == 2:
                            apex[next] = 1
                        queue.append(next)
                    else:
                        if apex[next] == apex[curr]:
                            print('NO')
                            end = True
                            break
                if end:
                    break
        if end:
            break
    else:
        print('YES')

