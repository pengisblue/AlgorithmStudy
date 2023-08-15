# Input 을 list 로 받음

# list 의 마지막 원소에서 시작 -> 원소를 [높이, 직전의 가장 높은 빌딩 좌표] 로  새로운 리스트에 pop

# 새로운 리스트의 최근 값(A)과 나머지 list 의 마지막 원소를 비교
  
# list의 마지막 원소가 작다면, A 를 가장 높은 빌딩 좌표 (temp_index)로 설정하여 [A, temp_index]의 형태로 저장

# list의 마지막 원소가 크다면, A 의 temp_index에 접근, A 이전에 A보다 컸던 빌딩과 list의 마지막 원소를 비교
     
# 위 과정을 반복하여 list의 마지막 원소보다 큰 빌딩(temp_index에 위치)을 찾아 [A, temp_index]의 형태로 저장
     
# 각 원소의 실제 index 값과 temp_index 값을 비교하여 사이에 총 몇 개의 빌딩이 있는지를 도출

N = int(input())
ls = []
ls_stack = []
cnt = 0
# input 을 list의 형태로 저장
for i in range(N):
    ls.append(int(input()))
# 새로운 list의 초기값 설정(맨 오른쪽 빌딩은 볼 수 있는 빌딩 x)
ls_stack.append([ls.pop(-1), -1])
# 초기값을 제외한 input 값들을 새로운 list에 할당
for i in range(N-1):
    temp_index = i
# 각 값들을 하나씩 pop 하여 temp_item으로 저장
# 원래 index 값을 temp_index로 저장
    temp_item = ls.pop(-1)
# temp_item 과 새로운 list의 마지막값(바로 오른쪽 빌딩)을 비교
# 만약, temp_item 이 더 크다면, temp_item 을 가장 큰 빌딩(좌표 = temp_index)로 설정
    while ls_stack[temp_index][0] < temp_item:
# 만약, temp_item의 좌표값이 -1 이라면, 맨 오른쪽까지 모든 빌딩을 확인가능한것
# 때문에, 현재 위치 index 값이 관찰 가능한 모든 빌딩의 갯수
        if ls_stack[temp_index][1] == -1:
            ls_stack.append([temp_item, -1])
            cnt += i +1
            break
# -1이 아니라면, temp_item보다 더 큰 빌딩이 나올때까지 temp_index를 기준으로 빌딩 좌표 탐색
        else:
            temp_index = ls_stack[temp_index][1]
# 새로운 list의 값이 더 크다면, temp_item이 관찰할 수 있는 빌딩이 더 이상 없음
    else:
        ls_stack.append([temp_item, temp_index])
        cnt += i - temp_index
print(cnt)