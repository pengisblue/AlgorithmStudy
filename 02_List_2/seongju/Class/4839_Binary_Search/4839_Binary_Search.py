# 4839 - 이진탐색
import sys
sys.stdin = open('input.txt')

def binarySearch(all_p, target) :
    l = 1
    r = int(all_p)
    cnt = 0

    while l <= r :
        mid = (l + r) // 2
        if mid > target :
            r = mid
            cnt += 1
        elif mid < target :
            l = mid
            cnt += 1
        elif mid == target :
            cnt += 1
            break

    return cnt


T = int(input())

for t in range(1, T+1) :
    P, Pa, Pb = map(int, input().split())
    a_result = binarySearch(P, Pa)
    b_result = binarySearch(P, Pb)

    if a_result < b_result :    # A의 탐색 횟수가 B보다 작은 경우
        print(f'#{t} A')
    elif a_result > b_result :
        print(f'#{t} B')
    else :
        print(f'#{t} 0')