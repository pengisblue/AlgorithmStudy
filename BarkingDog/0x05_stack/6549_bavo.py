import sys
input = sys.stdin.readline


while True:
    numbers_map = map(int, input().split())
    
    # 첫번째가 빌딩 개수임
    N = next(numbers_map)

    # 빌딩 개수 0이면 종료
    if N == 0:
        break

    numbers = list(numbers_map)

    numbers_stack = []

    # 제일 처음 가장 가까운 작은 수 인덱스가 없는 거를 numbers에서 pop해서 넣기
    numbers_stack.append( (numbers.pop(), -1 ))

    # 결과값으로 나올 최대 크기
    max_area = 0

    # 앞에서 하나 pop했으니 N-1번 반복
    for i in range(N - 1):

        # 숫자 하나 pop
        number = numbers.pop()

        # ***** 중요 ******
        # 스택의 끝에 있는 숫자보다 높은 숫자가 나오면 그냥 쌓아 올림
        # i에는 스택의 끝에 있는 도형의 위치이므로 number와 i를 튜플로 저장(list로 해도되는데 이게 더 편했음)
        # 스택의 사이즈가 변하더라도 아무튼 실질적 위치임 
        # 최종적으로 for문이 끝났을 때 스택에는 오름차순으로 값이 저장되어야 함
        # 왜 why for문이 끝났을 때 stack의 제일 처음 요소 == 모든 빌딩중 가장 낮은 놈 위치
        # 2번째 요소 == 모든 빌딩중 2번째로 낮은 놈위치 (여기서부턴 정확하지 않음 정확하게는 함께 셀 수 있는 빌딩 덩어리중 가장 낮은 놈의 가장 멀리뻗는? 인덱스)

        if numbers_stack and numbers_stack[-1][0] < number:
            numbers_stack.append( (number, i) )
            continue
        
        # 뽑은 놈이 스택의 제일 위에 있는 숫자보다 작을때 ( 스택의 제일 위에는 오름차순으로 해서 제일 높은 숫자가 저장되어 있음)
        # 그럼 뽑은 놈보다 작은거 나올때까지 pop때림 그리고 그 작은놈 기준으로 다시 오름차순 정렬이 될거임
        # 그리고 그값을 기준으로 뻗을 수 있는 최대한의 넓이를 계산해서 '1차적'으로 max_area를 갱신함
        while numbers_stack and numbers_stack[-1][0] >= number:
            height, lt_index = numbers_stack.pop()
            # print(height ,lt_index)
            width = i - lt_index
            max_area = max(max_area, height * width)
        
        numbers_stack.append((number, lt_index))
    
    # print(numbers_stack)

    # for문이 끝났을 때는 이제 오름차순으로 되어있고 N에서 인덱스위치를 빼면 같이 셀 수 있는 높이의 넓이가 나온다.
    # (그림으로 그리면 이해가 됨...)
    # 스택을 다털어서 max_area를 '2차 갱신함'
    while numbers_stack:
        height, idx = numbers_stack.pop()
        width = N - (idx + 1)
        max_area = max(max_area, height * width)
    

    # 제발
    print(max_area)


        