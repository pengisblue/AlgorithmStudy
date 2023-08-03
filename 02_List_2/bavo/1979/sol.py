import sys
sys.stdin = open('input.txt')



for i in range(int(input())):
    n,k=map(int,input().split())
    p=[input().replace(' ','') for _ in range(n)]
    p.extend([''.join(b) for b in list(zip(*p))])
    a=[b.split('0') for b in p]
    print(f'#{i+1} {sum([1 for i in range(len(a)) for j in range(len(a[i])) if len(a[i][j]) == k])}')
