#전기버스
#--보류--
ts=int(input())
for t in range(ts):
  k,n,m = map(int, input().split())
  elec = list(map(int, input().split()))
  count=-1
  total=[]
  start=0
  for i in elec:
    if n-k <= start:
      break
    elif start+k >=i:
      total.append(i)
      start = max(total)
      st=elec.index(start)
      elec = elec[st:]
      count+=1
    else:
      count=0

  print(f'#{t+1} {count}')
  