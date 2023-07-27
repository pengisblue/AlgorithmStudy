# 스택 수열

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
status = True

N = int(sys.stdin.readline())
n = 1

for i in range(N) :
    input_num = int(sys.stdin.readline())

    while n <= input_num :
        stack.push(n)
        n += 1
        answer.append('+')

    if stack.stackList[-1] == input_num :
        stack.pop()
        answer.append('-')
    else :
        status = False

if status == True :
    for j in answer :
        print(j)
elif status == False :
    print('NO')