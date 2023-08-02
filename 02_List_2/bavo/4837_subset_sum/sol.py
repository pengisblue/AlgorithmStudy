import sys

sys.stdin = open('input.txt')


def solution(depth, current_sum, current_idx):
    global num_of_elements, target, count

    if depth == num_of_elements:
        # print(current_sum)
        if current_sum == target:
            count += 1
        return

    for number in range(current_idx, 13):
        # solution(depth + 1, current_sum + ' ' +str(number), number + 1)
        solution(depth + 1, current_sum + number, number + 1)


for T in range(1, int(input()) + 1):
    num_of_elements, target = map(int, input().split())

    count = 0
    solution(0, 0, 1)

    print(f'#{T} {count}')
