import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
NGE = []        # 오큰수
stack = []      # 오큰수인지 판단할 수
for i in range(N):
    a = A.pop()     # 리스트 끝값부터 확인
    if stack:       # stack에 수가 있을 때
        while stack:    # stack이 비면 종료
            if stack[-1] > a:   # 오큰수이면
                NGE.append(stack[-1])   # 추가
                break
            else:   # 아니라면 오큰수가 될 수 없으므로 (pop 한 값 보다 왼쪽에 있으니)
                stack.pop()     # 리스트에서 제거
    if not stack:   # 비어있으면
        NGE.append(-1)      # 오큰수가 없으므로 -1
    if A and a > A[-1]:     # a가 바로 앞 원소보다 크면
        stack.append(a)     # 오큰수가 될 예정이므로 stack

NGE.reverse()
print(*NGE)
