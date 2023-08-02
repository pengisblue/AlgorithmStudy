
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0


N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

M = int(input())

is_subset = list(map(int,input().split()))

for num in is_subset:
    print(binary_search(numbers, num))
