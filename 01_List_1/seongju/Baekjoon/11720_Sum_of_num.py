# 숫자의 합

N = int(input())

T = list(map(int, input().rstrip()))
sum = 0
for i in T :
    sum += i
     
print(sum)