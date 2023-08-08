import sys

input = sys.stdin.readline

n = int(input())

histogram = []

for _ in range(n):
    histogram.append(int(input()))

stack = [(histogram[0], 0)]

max_square = 0

for i in range(1, n):
    # 스택은 오름차순으로 정렬될 예정인데
    # 자기보다 낮은게 나올때마다 넓이를 계산하고 깎는다
    # 자기보다 높은게 낮으면 그냥 안보고 넣는다
    # 맨 마지막에 높은게 나와도 반대편 계산은 나중에 한다`
    if stack and stack[-1][0] < histogram[i]:
        stack.append( (histogram[i], i))

    while stack and stack[-1][0] >= histogram[i]:
        height, idx = stack.pop()
        width = i - idx
        max_square = max(max_square, height * width)

    stack.append((histogram[i], idx))

for height, index in stack:
    max_square = max(max_square, (n - index) * height)

print(max_square)