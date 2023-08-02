#소트인사이드
n=int(input())
k=[]
for i in str(n):
  k.append(int(i))
  k.sort(reverse=True)
for i in range(len(k)):
  re=''
  re += str(k[i])
  print(re, end='')