#버블 소트
n=int(input())
arr=[]
for i in range(n):
  num=int(input())
  arr.append(num)

def BubbleSort(arr, n):
  for i in range(n-1, 0, -1):
    c=False
    for j in range(0, i):
      if arr[j] > arr[j+1]:
        c=True
        arr[j], arr[j+1] = arr[j+1], arr[j]
    if not c:
      return n-i     
  
res = BubbleSort(arr, n)
print(res)
#--시간초과--