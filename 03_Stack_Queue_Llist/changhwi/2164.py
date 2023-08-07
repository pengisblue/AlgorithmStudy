n=int(input())
from collections import deque
a=deque()
for i in range(1,n+1):
  a.append(i)

for i in range(n-1):
  a.popleft()
  a.append(a.popleft())
print(a[0])