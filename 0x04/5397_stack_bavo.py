# 스택으로 푼거
T = int(input())

for _ in range(T):
    
    input_text = input()
    #커서의 왼쪽에 있는 문자열
    left_cursor = []
    #커서의 오른쪽에 있는 문자열(역순으로 들어옴)
    right_cursor = []
    
    for char in input_text:
        #커서 왼쪽으로 옮기기
        if char == '<':
            if len(left_cursor) > 0:
                # 왼쪽커서에 요소가 남아 있으면 pop해서 오른쪽에 append
                right_cursor.append(left_cursor.pop())
        elif char == '>':
        #커서 오른쪽으로 옮기기
            if len(right_cursor) > 0:
                # 오른쪽 커서에 요소가 남아 있으면 pop해서 오른쪽에 append
                left_cursor.append(right_cursor.pop())
        elif char == '-':
            #지울땐 커서의 왼쪽에 있는 애를 그냥 pop해주면 됨
            if len(left_cursor) > 0:
                left_cursor.pop()
        else:
            # 입력이 들어오면 커서의 왼쪽의 끝에 append해주면 됨
            left_cursor.append(char)
    
    # 왼쪽커서의 요소에 오른쪽커서를 뒤집은 배열을 연결
    left_cursor.extend(right_cursor[::-1])
    # 출력
    print(''.join(left_cursor))