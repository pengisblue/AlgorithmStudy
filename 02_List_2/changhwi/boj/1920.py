# 수 찾기
def binary_search(array, target, start, end):
  while start<= end:
    mid = (start + end)//2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid-1
    else:
      start = mid+1
  return None

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
a.sort()
for i in b:
  result=binary_search(a, i, 0, n-1)
  if result != None:
    print(1)
  else:
    print(0)