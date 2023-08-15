import sys
input = sys.stdin.readline

N = int(input())

rooftop = []

# 인풋받아 배열 초기화
for _ in range(N):
    rooftop.append(int(input()))

#결과카운트
cnt = 0

# 루프탑 스택에는 [높이, 제일 가까운 못보는 빌딩의 index가 있음]
# 인풋의 오른쪽 끝부터 시작해야함. 첫빌딩 만들어놓고 시작. 첫 빌딩은 제일 끝이므로 못보는 빌딩이 -1임
rooftop_stack = []
rooftop_stack.append([rooftop.pop(), -1])

for i in range(len(rooftop)):
    # 제일 먼저 빌딩 높이를 pop
    building = rooftop.pop()
    
    # i == len(rooftop_stack) -1임. 즉, 금방 pop한 building이 append될 인덱스의 바로 이전 인덱스임 == 바로 앞의 빌딩
    # temp_index는 유동적으로 변하면서 제일 끝까지 가거나, building보다 높거나 같은 빌딩을 만나면 멈춤
    temp_index = i

    # 제일 끝에 도착(처음 넣은 빌딩의 가장 가까운 높은 빌딩 index로 -1을 지정해놨음)하거나
    # building보다 높거나 같은 인덱스에 도착했을 경우 temp_index엔 그 빌딩의 인덱스가 담김
    while temp_index != -1 and rooftop_stack[temp_index][0] < building:
        temp_index = rooftop_stack[temp_index][1]
    
    # N(== i + 1)번째로 들어온 빌딩이 볼 수 있는건 temp_index ~ i번째 빌딩까지의 개수
    cnt += i - temp_index

    # 빌딩높이와 가장가까운 높은 빌딩 인덱스를 담아 append
    rooftop_stack.append([building, temp_index])

print(cnt)