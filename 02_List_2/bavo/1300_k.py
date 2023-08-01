
size = int(input())

k = int(input())

left = 1
right = min(int(1e9), size ** 2)


while left < right:
    mid = (left + right) // 2

    # sum_of_lt = 0

    sum_of_lt = sum([min(mid // i, size) for i in range(1, size + 1)])
    # for i in range(1, size + 1):
    #     sum_of_lt += min(mid // i, size)
    #     if sum_of_lt > k:
    #         break
    
    
    if sum_of_lt >= k:
        right = mid
    else:
        left = mid + 1
    
print(left)