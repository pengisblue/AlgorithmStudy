import sys

sys.stdin = open('input.txt')


def bubble_sort(arr):  # 버블 소트 함수 구현
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


T = int(input())  # 테스트 케이스 개수

for t in range(1, T + 1):
    N = int(input())  # 정수의 개수
    ai = list(map(int, input().split()))  # N 개의 정수 ai

    sort_list = bubble_sort(ai)  # 오름차순 정렬
    answer = []

    for i in range(5) :
        answer.append(sort_list[-i - 1])        # 앞 값
        answer.append(sort_list[i])         # 뒷 값

    print(f'#{t}', *answer)