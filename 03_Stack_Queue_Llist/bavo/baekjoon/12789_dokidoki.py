# 도키도키 간식드리미

def solution(arr, number):
    stack = []

    curr_index = 1
    for i in range(number):
        stack.append(arr[i])

        while stack and stack[-1] == curr_index:
            curr_index += 1
            stack.pop()

    if stack:
        return 'Sad'
    else:
        return 'Nice'


N = int(input())
students = list(map(int, input().split()))

print(solution(students, N))
