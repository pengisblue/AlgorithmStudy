
def num_of_one(number):
    count = 0
    while number > 0:
        count += number % 2
        number //= 2

    return count


for T in range(int(input())):

    size, target = map(int,input().split())

    count_of_set = 0

    for x in range(1 << 12):
        if num_of_one(x) != size:
            continue

        sum_of_set = 0

        for y in range(12):
            if x & (1 << y):
                print(y + 1, end=' ')
                sum_of_set += y + 1
        print()
        if sum_of_set == target:
            count_of_set += 1

    print(f'#{T+1} {count_of_set}')

