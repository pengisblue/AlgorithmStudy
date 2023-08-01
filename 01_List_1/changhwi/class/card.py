#숫자카드
n=int(input())
for j in range(n):
  m=int(input())
  num = list(map(str, input()))
  num1 = list(map(int, num))
  total=[]
  num1.sort()
  for i in num1:
    total.append(num1.count(i))
    res1 = max(total)
    if num1.count(i) == res1:
      res2 = i
  print(f'#{j+1} {res2} {res1}')