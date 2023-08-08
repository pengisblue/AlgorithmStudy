from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
que = PriorityQueue()
for i in range(N):
    x = int(input())
    if x == 0:
        if que.empty():
            print(0)
        else:
            get = que.get()     # (절대값 x, x)로 나오므로
            print(get[1])       # 튜플의 인덱스 1값만 출력
    else:
        que.put((abs(x), x))    # (절대값 x, x)로 정렬하면 음수 x가 우선 정렬
