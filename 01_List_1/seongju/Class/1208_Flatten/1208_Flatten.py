# 1208 - Flatten
import sys
sys.stdin = open('input_Flatten.txt')

T = 10

for t in range(T) :
    N = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    sort_list = [0] * (100) # 정렬된 배열
    cnt = [0] * (101)   # 카운트

    for i in range(0, len(data)) :
        cnt[data[i]] += 1

    for j in range(1, len(cnt)) :
        cnt[j] += cnt[j-1]

    for k in range(len(data)) :
        cnt[data[k]] -= 1
        sort_list[cnt[data[k]]] = data[k]

    min_n = sort_list[0]
    max_n = sort_list[-1]

    for n in range(N):
        sort_list[cnt[max_n] - 1] -= 1
        sort_list[cnt[min_n] - 1] += 1
        cnt[max_n] -= 1
        cnt[min_n] += 1

        min_n = sort_list[0]
        max_n = sort_list[-1]


        if max_n - min_n <= 1:
            break

    '''
    for n in range(N) :
        sort_list[cnt[max_n]] -= 1
        sort_list[cnt[min_n+1]-1] += 1
        cnt[max_n] += 1
        cnt[min_n + 1] -= 1

        min_n = sort_list[0]
        max_n = sort_list[-1]

        if max_n - min_n <= 1 :
            break
    '''
    print(f'#{t+1} {max_n - min_n}')

