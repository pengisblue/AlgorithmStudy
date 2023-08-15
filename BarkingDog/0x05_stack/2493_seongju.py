# 스택 - 탑

import sys

class Stack() :
    def __init__(self) :
        self.stackList = []

    def push(self, data) :
        self.stackList.append(data)

    def pop(self) :
        pop_object = None
        pop_object = self.stackList.pop()
        return pop_object
    
stack = Stack()

answer = []
N = int(sys.stdin.readline())
towel = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    while stack.stackList :
        if stack.stackList[-1][1] > towel[i]:
            answer.append(stack.stackList[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack.stackList :
        answer.append(0)

    stack.push([i, towel[i]])

print(" ".join(map(str, answer)))