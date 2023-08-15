import sys
input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N):
    number = int(input())
    if number == 0:
        #잘못쓰면 지워야지
        numbers.pop()
    else:
        numbers.append(number)

print(sum(numbers))