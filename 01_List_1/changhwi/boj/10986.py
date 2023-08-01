# 나머지 합
n, m = map(int, input().split())
num = list(map(int, input().split()))
count=0
for i in range(n):
  for j in range(i,n):
    if sum(num[i:j+1]) % m == 0:
      #print(num[i:j+1])
      count+=1
print(count)
#--시간초과