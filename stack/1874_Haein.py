import sys
input = sys.stdin.readline

# pop & append
def pop_append(pop_list, append_list):
    pop_num = pop_list.pop()
    append_list.append(pop_num)

n = int(input())
sequence = [int(input()) for i in range(n)]
numbers = [i for i in reversed(range(1, n + 1))]  # 수열을 만들어볼 숫자list
push_tmp = []  # + 될 때 append
pop_tmp = []  # - 될 때 append
results = []  # 출력 값 저장 list
index = 0
is_sequence = True

while index < n:  # 수열이 완성될 때 까지
    if push_tmp and push_tmp[-1] > sequence[index]:  # 수열을 만들 수 없는 조건
        is_sequence = False
        break
    elif push_tmp and push_tmp[-1] == sequence[index]:
        pop_append(push_tmp, pop_tmp)
        results.append('-')
        index += 1
    else:
        for i in range(len(numbers)):
            num = numbers[-1]
            pop_append(numbers, push_tmp)
            results.append('+')
            if num == sequence[index]:
                break
        pop_append(push_tmp, pop_tmp)
        results.append('-')
        index += 1

if is_sequence:
    for result in results:
        print(result)
else:
    print('NO')