# pop 과 push 만 구현한다면 쉽게 풀 수 있음!

import sys
input = sys.stdin.readline

class stack:
    def __init__(self):
        self.top = []
    
    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.empty():
            return self.top.pop(-1)
        else:
            return -1

stk = stack()

K = int(input())
for i in range(K):
    num = int(input())
    if num == 0:
        stk.pop()
    else:
        stk.push(num)

print(sum(stk.top))