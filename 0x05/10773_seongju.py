# 스택 - 제로

import sys

class Stack() :
    def __init__(self) :
        self.stack = []

    def push(self, data) :
        self.stack.append(data)
        return self.stack

    def pop(self) :
        pop_object = None
        pop_object = self.stack.pop()
        return pop_object
    
    
stack_ = Stack()
N = int(sys.stdin.readline())

for i in range(N) :
    input_num = int(sys.stdin.readline())
    if input_num == 0 :
        stack_.pop()
    else :
        stack_.push(input_num)

print(sum(stack_.stack))