#합
for ts in range(10):
  n = int(input())
  arr = [list(map(int, input().split()))for _ in range(100)]
  sum_num1=[]
  sum_num2=[]

  col_sum=0
  for i in range(100):
    col_sum = sum(arr[i])
    sum_num1.append(col_sum)
  col_max = max(sum_num1)
  #print(col_max)

  for j in range(100):
    row_sum=0
    for i in range(100):
      row_sum += arr[i][j]
    sum_num2.append(row_sum)
  row_max = max(sum_num2)
  #print(row_max)

  cross_num=0
  for i in range(100):
    cross_num += arr[i][i]
  #print(cross_num)

  cross_num1=0
  for i in range(100):
    cross_num1 += arr[i][99-i]
  #print(cross_num1)

  res = max(col_max, row_max, cross_num, cross_num1)
  print(f'#{ts+1} {res}')