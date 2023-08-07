from collections import deque

t = int(input())
dq = deque(enumerate(map(int, input().split())))
# 인덱스 설
result = []

while dq:
    index, number = dq.popleft()
    result.append(index + 1)

# collections 모듈의 deque 클래스에는 rotate() 함수가 있습니다.
# rotate() 함수는 덱의 원소들을 주어진 값만큼 오른쪽이나 왼쪽으로 회전시킵니다.
# 이를 통해 덱의 원소들을 순환시키거나 특정한 위치로 이동시킬 수 있습니다.

    if number > 0:
        dq.rotate(-(number - 1))
    else:
        dq.rotate(-number)

print(" ".join(map(str, result)))


