# DNA비밀번호
n, m = map(int, input().split())
str = list(input())
num = list(map(int, input().split()))
count = 0

for i in range(n - m + 1):
    code = str[i:i + m]
    if (code.count('A') >= num[0]) and (code.count('C') >= num[1]) and (code.count('G') >= num[2]) and (code.count('T') >= num[3]):
        count += 1

print(count)

#--시간초과--