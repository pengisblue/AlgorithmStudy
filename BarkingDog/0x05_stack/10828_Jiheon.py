# python 의 list를 이용해 stack 자료구조형과 유사한 자료구조를 형성

import sys
input = sys.stdin.readline

class stack:
    def __init__(self):
        self.top = []
    
    def size(self):
        return len(self.top)
    
    def empty(self) -> bool :
        return len(self.top) == 0
    
    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.empty():
            return self.top.pop(-1)
        else:
            return -1
    
    def peek(self):
        if not self.empty():
            return self.top[-1]
        else:
            return -1


stk = stack()

N = int(input())
for _ in range(N):
    i = list(input().split())
    if i[0] == 'pop':
        item = stack.pop(stk)
        print(item)
    elif i[0] == 'size':
        print(stack.size(stk))
    elif i[0] == 'top':
        print(stack.peek(stk))
    elif i[0] == 'empty':
        if stack.empty(stk) == True:
            print(1)
        else:
            print(0)
    else:
        stack.push(stk, i[1])