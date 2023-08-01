#뷰
for j in range(10):
  n=int(input())
  count=0
  list1 = list(map(int, input().split()))
  for i in range(2,len(list1)-2):
    side=[]
    side.append(list1[i-2])
    side.append(list1[i-1])
    side.append(list1[i+1])
    side.append(list1[i+2])
    side_max=max(side)
    if list1[i] > side_max:
      count+=(list1[i]-side_max)
  print(f'#{j+1} {count}')