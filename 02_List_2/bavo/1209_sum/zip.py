

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for number in numbers:
    print(number)

print('#' * 50)

zip_numbers = list(zip(*numbers))

for number in zip_numbers:
    print(number)

