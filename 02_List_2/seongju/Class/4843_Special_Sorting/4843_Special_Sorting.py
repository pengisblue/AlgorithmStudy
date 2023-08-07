# 4843 - 특별한 정렬
import sys
sys.stdin = open('input.txt')

def bubble_sort(arr) :      # 버블 소트 함수 구현
    n = len(arr)

    for i in range(n) :
        for j in range(n-1-i) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

T = int(input())        # 테스트 케이스 개수

for t in range(1, T+1) :
    N = int(input())        # 정수의 개수
    ai = list(map(int, input().split()))    # N 개의 정수 ai

    sort_list = bubble_sort(ai)     # 오름차순 정렬
    answer = []
    l = 0       # 시작 인덱스
    r = N - 1       # 마지막 인덱스
    cnt = 1     # 순서 변수 선언
    
    while cnt <= 10 :       # 정렬된 숫자 10개까지만 출력
        if cnt % 2 == 1 :       # 순서가 홀수 번째일 때 큰 값 추출
            answer.append(sort_list[r])
            r -= 1      # 오른쪽 인덱스를 앞으로 한 칸 당겨준다.
            cnt += 1    # 카운트 +1
        elif cnt % 2 == 0 :     # 순서가 짝수 번째일 때 작은 값 추출
            answer.append(sort_list[l])
            l += 1      # 왼쪽 인덱스를 뒤로 한 칸 밀어준다.
            cnt += 1        # 카운트 +1

    print(f'#{t} {" ".join(map(str, answer))}')
