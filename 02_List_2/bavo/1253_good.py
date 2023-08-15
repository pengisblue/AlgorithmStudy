def binary_sarch(arr, target, left, right):

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return -1

def only_zero(arr):
    for num in arr:
        if num != 0:
            return False
    
    return True

def count_sum_of_two_elements(nums):
    global n
    good_count = 0

    if only_zero(nums):
        return n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            idx = binary_sarch(nums, nums[i] - nums[j] , 0 , n - 1)
            if idx >= 0 and idx != i and idx != j:
                good_count += 1
                print(i)
                break
            


    return good_count


n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

result = count_sum_of_two_elements(numbers)
print(result)


