# 수 정렬하기
n=int(input())
k=[]
for i in range(n):
  m=int(input())
  k.append(m)
  k.sort()
for i in range(n):
  print(k[i])
  