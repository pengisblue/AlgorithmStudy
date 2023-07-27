import sys

input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N):
    numbers.append(int(input()))

numbers_stack = []

count = 0
# 높이, 가장 가까운 나보다 높은 놈 index , 마주친거중 나랑 같은 놈 개수
numbers_stack.append([numbers.pop(), -1, 0])

# result = []

for i in range(N - 1):
    number = numbers.pop()
    
    temp_index = i

    num_of_same = 0
    temp_count = 0

    # 오큰수를 찾는다...
    while temp_index != -1 and numbers_stack[temp_index][0] <= number:
        # 만약 나랑 같은 숫자면 걔가 가지고 있는 '오큰수를 만나기전 자신과 같은 수의 개수'에 1을 더한 값을 저장하면서 count에 더한다
        if numbers_stack[temp_index][0] == number:
            num_of_same = numbers_stack[temp_index][2] + 1
            temp_count += num_of_same
        else:
            # 같지 않으면 해당 수 1개 + 걔 뒤에 있는 같은 수 갯수를 더함
            temp_count += 1 + numbers_stack[temp_index][2]
        # 해당 수의 오큰수로 인덱스 이동
        temp_index = numbers_stack[temp_index][1]

    # 위의 while문 돌았을 때 마지막까지 탐색하거나 자기보다 큰 숫자 만났을 때가 카운트 안되어서 한개 추가
    if temp_index != -1 and numbers_stack[temp_index][0] > number:
        temp_count += 1

    count += temp_count

    # result.append(temp_count)

    # 해당 숫자로 탐색 끝나면 [숫자, 오큰수인덱스, 오큰수 만나기전 같은 수 개수]를 리스트로 저장
    numbers_stack.append([number, temp_index, num_of_same])


# print(numbers_stack)
# print(result)
print(count)