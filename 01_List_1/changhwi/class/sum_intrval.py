#구간합
n=int(input())
for k in range(n):
    sum_num=[]
    count, m = map(int,input().split())
    num = list(map(int, input().split()))
    for i in range(count-m+1):
        total=[]
        for j in range(i,i+m):
            total.append(num[j])
        sum_num.append(sum(total))
#print(sum_num)
    res = max(sum_num) - min(sum_num)
    print(f'#{k+1} {res}')