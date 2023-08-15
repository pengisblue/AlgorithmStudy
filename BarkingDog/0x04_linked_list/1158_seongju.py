# 요세푸스

N, K = map(int,input().split())

answer= []
arr = [i for i in range(1, N+1)]
num = 0

for i in range(N):
    num += (K-1)

    if num >= len(arr):
        num %= len(arr)

    answer.append(str(arr[num]))
    arr.pop(num)

print("<",', '.join(answer),">", sep="")