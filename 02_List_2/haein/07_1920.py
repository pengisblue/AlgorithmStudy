N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

for number in B:
    s_idx = 0           # 시작 인덱스
    e_idx = N - 1       # 종료 인덱스
    while s_idx <= e_idx:
        m_idx = (s_idx + e_idx)//2
        mid = A[m_idx]
        if mid > number:  # 찾는 숫자가 더 작으면 end를 앞으로
            e_idx = m_idx - 1
        elif mid < number:  # 찾는 숫자가 더 크면 start를 뒤로
            s_idx = m_idx + 1
        else:
            print(1)
            break
    if s_idx > e_idx:
        print(0)
