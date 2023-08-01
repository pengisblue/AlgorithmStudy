#플래튼
for i in range(10):

  n=int(input())
  numbers = list(map(int, input().split()))
  for _ in range(n):
    numbers.append(max(numbers)-1)
    numbers.remove(max(numbers))
    numbers.append(min(numbers)+1)
    numbers.remove(min(numbers))


  res = max(numbers) - min(numbers)
  print(f'#{i+1} {res}')