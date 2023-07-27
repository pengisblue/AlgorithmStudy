# Stack 을 사용하여 해결 가능
  
# Stack 에 탑의 높이와 위치 정보를 dictionary 형태로 저장

# 탑의 높이가 Stack의 peek보다 크다면, Stack 의 peek 값이 input 보다 클 때 까지 pop 반복

# peek 값이 탑의 높이 보다 크거나 더 pop할 것이 없을 경우에, peek의 value 에 저장된 위치 정보 호출

# input이 모두 처리될 때 까지 반복.

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
            return {0:0}
    
    def empty(self) -> bool:
        return len(self.top) == 0

skt = stack()

N = int(input())
ls = list(map(int, input().split()))

# list로 저장한 input 값을 하나씩 반복
for i in range(len(ls)):
        # dict 형태로 저장된 stack 의 peek 값에서 value 값 즉 높이를 호출, input 탑의 높이와 비교
        # peek의 높이가 더 클 경우, peek 값의 key 값 즉 위치 정보를 print
        if list(skt.peek().values())[0] >= ls[i]:
            print(list(skt.peek().keys())[0], end = ' ')
            skt.push({i+1:ls[i]})
        # input의 높이가 더 클 경우, peek 값을 pop하면서 input보다 높은 peek 값을 찾음.
        # 더 큰 peek 값을 찾았거나, stack 의 끝까지 찾지 못했다면, 위치정보를 호출.
        else:
            while list(skt.peek().values())[0] < ls[i] and list(skt.peek().values())[0] != 0:
                skt.pop()
            print(list(skt.peek().keys())[0], end = ' ')
            skt.push({i+1:ls[i]})