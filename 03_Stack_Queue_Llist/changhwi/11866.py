from collections import deque

a = deque()
b=[]
n, m = map(int, input().split())
for i in range(1, n+1):
  a.append(i)

while a:
  for i in range(m-1):
    a.append(a.popleft())
  b.append(a.popleft())

print('<', end='')
[print(f'{b[i]},', '', end='') for i in range(n-1)]
print(b[-1], end='')
print('>')