# Day1 - View

'''
고려사항
- 양쪽 끝 2개씩 높이 -> 0
- 본인 기준 양쪽 두개 비교
'''
import sys

T_num = 10

for r in range(T_num) :
    N = int(sys.stdin.readline())   # 가로 길이
    T = list(map(int, sys.stdin.readline().split()))    # 빌딩 높이
    count = 0

    for i in range(2, N-2) : # n번째 테스트 케이스(양쪽 끝 2개씩 제외)
        if ((T[i] > T[i-1]) and (T[i] > T[i+1]) and (T[i] > T[i-2]) and (T[i] > T[i+2])) :
            min_v = 255
            view_list = []

            for k in range(-2, 3): # 양쪽 두 칸씩 비교
                view_list.append(T[i] - T[i+k])
            
            for j in view_list :    # min값 결정
                if min_v > j and j > 0 :  # 0 값은 자기 자신이니까 제외
                    min_v = j   # 양 옆 두칸과의 높이 차이 중 가장 적게 차이 나는 값

            count += min_v
                        
    print(f'#{r+1} {count}')