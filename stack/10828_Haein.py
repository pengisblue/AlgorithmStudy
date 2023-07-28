import sys
input = sys.stdin.readline

# 명령어를 실행시킬 함수
def com_push(stack_list, com, num = None):  # stack할 list, 명령어, 숫자(필요할 경우)를 매개변수로 받음
    if com == 'push':  # 숫자 push
        stack_list.append(num)
    elif com == 'pop':
        if len(stack_list) == 0:  # pop할 숫자가 없으면 -1을 출력
            print(-1)
        else:
            pop_int = stack_list.pop()
            print(pop_int)
    elif com == 'size':
        print(len(stack_list))
    elif com == 'empty':  # isempty == 1 isnotempty == 0
        if stack_list:
            print(0)
        else:
            print(1)
    elif com == 'top':  # top을 출력 / 없으면 -1
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])


N = int(input())
stack = []
for i in range(N):
    command = input().split()
    if len(command) == 1:  # push가 아닌 경우
        com = command[0]
        com_push(stack, com)
    else:  # push인 경우
        com, num = command[0], int(command[1])
        com_push(stack, com, num)

# class Stack:
#     stack_list = []

#     def __init__(self, X = None):
#         self.X = X
#         Stack.stack_list = []

#     def push_stack(self, X):
#         Stack.stack_list.append(self.X)

#     def pop_stack(self):
#         if Stack.stack_list:
#             Stack.num = Stack.stack_list.pop()
#             print(Stack.num)
#         else:
#             print(-1)

#     def size_stack(self):
#         print(len(Stack.stack_list))

#     def empty_stack(self):
#         if Stack.stack_list:
#             print(0)
#         else: print(1)
    
#     def top_stack(self):
#         if Stack.stack_list:
#             print(Stack.stack_list[-1])
#         else:
#             print(-1)


# N = int(input())
# stack = Stack()
# for i in range(N):
#     act = input().split()
#     if len(act) == 1:
#         command = act[0]
#         if command == 'pop':
#             stack.pop_stack()
#         elif command == 'size':
#             stack.size_stack()
#         elif command == 'empty':
#             stack.empty_stack()
#         else: stack.top_stack()
#     else:
#         num = act[1]
#         stack.push_stack(num)