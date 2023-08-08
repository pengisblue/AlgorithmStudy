from queue import PriorityQueue
import sys

input = sys.stdin.readline

qre = PriorityQueue()

n = int(input())

for i in range(n):
    temp = int(input())
    if not qre.empty() and temp == 0:
        print(qre.get()[1])
    elif qre.empty() and temp == 0:
        print('0')
    else:
        qre.put((abs(temp), temp))


