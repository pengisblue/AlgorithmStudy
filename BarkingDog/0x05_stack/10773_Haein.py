import sys
input = sys.stdin.readline

K = int(input())
numbers = []
for i in range(K):
    num = int(input())
    if not num:
        numbers.pop()
    else:
        numbers.append(num)

print(sum(numbers))