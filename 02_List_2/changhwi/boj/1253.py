#좋다 -- 보류
n=10
numbers=list(map(int, input().split()))
numbers.sort()
count=0
if 0 in numbers:
  count = n-1
else:
  for i in range(n):
    start=0
    end=n-1
    while True:
      if start >= end:
        break
      elif numbers[start] + numbers[end] < numbers[i]:
        end-=1
      elif numbers[start] + numbers[end] > numbers[i]:
        start+=1
      elif numbers[start] + numbers[end] == numbers[i]:
        count+=1
        start+=1