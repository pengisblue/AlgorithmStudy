N = int(input())
M = int(input())  # 합해서 나온 수
numbers = list(map(int, input().split()))  # 합할 숫자 리스트
numbers.sort()  # 정렬
small, big = 0, -1
result = 0  # 합한 결과
cnt = 0

while numbers[small] < numbers[big]:
    result = numbers[small] + numbers[big]
    if result == M:
        cnt += 1
        small += 1
        big -= 1
    elif result < M:
        small += 1
    else:
        big -= 1

print(cnt)
