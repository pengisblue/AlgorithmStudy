#민맥스
n=int(input())
for i in range(n):
    m=int(input())
    num=list(map(int, input().split()))
    print(f'#{i+1} {max(num)-min(num)}')
#--내장함수 사용--