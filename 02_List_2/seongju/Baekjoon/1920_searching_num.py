# 1920 - 수 찾기
import sys
input = sys.stdin.readline

N = int(input())   # A의 길이(원본)
A = list(map(int, input().split()))
A.sort()

M = int(input()) # 찾을 값 리스트의 길이
m_list = list(map(int, input().split()))


for i in m_list :
    start = 0
    end = N-1

    while start <= end :
        mid = (start + end) // 2
        if A[mid] > i :
            end = mid - 1
        elif A[mid] < i :
            start = mid + 1
        elif A[mid] == i :
            print(1)
            break

        if (mid == start or mid == end) and A[mid] != i :
            print(0)