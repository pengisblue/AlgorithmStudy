def binary_search(num, target):
    left = 1
    right = num
    count = 1
    while left <= right:
        mid = (left + right) // 2
        if mid == target:
            return count
        elif mid > target:
            right = mid
        elif mid < target:
            left = mid
        count += 1
    return count


for T in range(int(input())):
    p, a, b = map(int, input().split())
    x = binary_search(p, a)
    y = binary_search(p, b)
    print(f'#{T + 1} {"A" if y > x else "0" if x == y else "B"}')
