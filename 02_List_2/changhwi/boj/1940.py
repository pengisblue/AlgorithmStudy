# 주몽
n=int(input())
m=int(input())
count=0
numbers = list(map(int, input().split()))
numbers.sort()
i=0
j=n-1
while True:
  if i >= j:
    break
  elif numbers[i] + numbers[j] == m:
    count+=1
    i+=1
    j-=1
  elif numbers[i] + numbers[j] < m:
    i+=1
  else:
    j-=1
print(count)