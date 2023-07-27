import sys
input = sys.stdin.readline

result = []
numbers = []

n = int(input())

for _ in range(n):
    numbers.append(int(input()))

# 정수가 순서대로 하나씩 주어짐 그 index
index = 1

for number in numbers:
    # index보다 주어진 넘버가 크면 우선 그 숫자만큼 push를 해야함
    while index <= number:
        numbers.append(index)
        result.append('+')
        index += 1
    
    # 스택의 제일 위에 있는게 주어진 숫자면 pop하면 됨
    if numbers[-1] == number:
        numbers.pop()
        result.append('-')
    else:
    # 스택은 제일 위에거만 뽑을 수 있어서 제일 위에 없는 순간 더 큰수 아니면 못뽑음
        print('NO')
        break
else:
    print('\n'.join(result))