#부분집합
A=list(range(1,13))
#print(A)
ts=int(input())
for ts in range(ts):
  res=[]
  count=0
  n, k = map(int, input().split())


  for i in range(1<<12):
    total=[]
    for j in range(12):
      if i&(1<<j):
        total.append(A[j])
    res.append(total)
  #print(res)


  for sub in res:
    if sum(sub) == k and len(sub) == n:
      print(sub)
      count+=1

  print(f'#{ts+1} {count}')