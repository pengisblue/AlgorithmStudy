# push 와 pop 만 구현할 수 있으면 쉽게 풀 수 있음!

import sys
input = sys.stdin.readline

class stack:
    def __init__(self):
        self.top = []

    
    def push(self, item):
        self.top.append(item)
    
    def pop(self):
        self.top.pop(-1)
    
    def peek(self):
        if not self.empty():
            return self.top[-1]
        else:
            return 0
    
    def empty(self) -> bool:
        return len(self.top) == 0

N = int(input())
stk = stacK()
j = 1
for i in range(1, N+1):
    num = int(input())
    if stk.peek() <= num:
        while stk.peek() <=num:
            stk.push(j)
            j += 1
            print('+')
    else:
        stk.pop()
        print('-')