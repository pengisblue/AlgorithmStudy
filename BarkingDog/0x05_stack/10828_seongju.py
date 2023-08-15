# 스택
import sys

N = int(sys.stdin.readline())
a = [None] * N

idx = - 1

def push(n) :
    global idx, a
    idx += 1
    a[idx] = n
    
def pop() :
    global idx, a
    if (idx == -1 and a[idx] == None) :
        return -1
    else :
        idx -= 1
        return a[idx+1]

def size() :
    global idx, a
    if idx == -1 :
        return 0
    else :
        return len(a[0:idx+1])

def empty() :
    global idx, a
    if idx == -1 :
        return 1
    else :
        return 0
    
def top() :
    global idx, a
    if idx == -1 :
        return -1
    else :
        return a[idx]


for i in range(N) :
    user_input = list(sys.stdin.readline().split())
    if user_input[0] == 'push' :
        push(user_input[1])
    elif user_input[0] == 'pop' :
        print(pop())
    elif user_input[0] == 'size' :
        print(size())
    elif user_input[0] == 'empty' :
        print(empty())
    elif user_input[0] == 'top' :
        print(top())