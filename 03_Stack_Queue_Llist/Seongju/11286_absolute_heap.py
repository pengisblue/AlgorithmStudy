# 11286 - 절댓값 힙
import sys
from queue import PriorityQueue

q = PriorityQueue()

N = int(sys.stdin.readline())

for i in range(1, N+1) :
    A = int(sys.stdin.readline())
    if A > 0 :
        q.put((A, A))
    elif A < 0 :
        q.put((-A, A))
    else :
        if q.empty() == True :
            print(0)
        else :
            print(q.get()[1])



