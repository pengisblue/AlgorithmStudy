N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))
for i in range(N-1, 0, -1):
    for j in range(i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
for i in range(N):
    print(numbers[i])
