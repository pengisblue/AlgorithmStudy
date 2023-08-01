#평균
n = int(input())
a=[]
real_a=list(map(int, input().split()))
M=max(real_a)
for i in real_a:
    b = (i/M)*100
    a.append(b)
print(sum(a)/n)