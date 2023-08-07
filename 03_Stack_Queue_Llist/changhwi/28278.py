#28278
# import sys
# input = sys.stdin.readline

stack = []
t= int(input())
for i in range(t):
  N=list(map(int, input().split()))
  if N[0] == 1:
    stack.append(N[1])
  elif N[0] == 2:
    if len(stack)>0:
        print(stack.pop())
    else:
      print(-1)
  elif N[0] == 3:
    print(len(stack))
  elif N[0] == 4:
    if stack==[]:
      print(1)
    else:
      print(0)
  elif N[0] == 5:
    if len(stack)>0:
      print(stack[-1])
    else:
      print(-1)