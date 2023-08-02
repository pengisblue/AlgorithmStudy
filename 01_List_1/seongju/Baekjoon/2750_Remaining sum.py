# 수 정렬하기

N = int(input())
num_list = []

for i in range(N) :
    num_list.append(int(input()))
    
for k in range(len(num_list)) :
    for j in range(N-1) :
        if num_list[j] > num_list[j+1] :
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp
        
for n in num_list :
    print(n)