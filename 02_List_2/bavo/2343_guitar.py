def make_blueray(total, size, arr):

    blueray_count = 0
    temp_index = len(arr) - 1
    while blueray_count < total:
        temp_sum = 0
        while temp_index >= 0 and temp_sum + arr[temp_index] <= size:
            temp_sum += arr[temp_index]
            temp_index -= 1
        if temp_index < 0:
            return True
        else:
            blueray_count += 1
    return False


N, M = map(int, input().split())

lectures = list(map(int, input().split()))


left = 1
right = sum(lectures)

last_index = right
while left <= right:

    mid = (left + right) // 2

    if make_blueray(M, mid, lectures):
        last_index = mid
        right = mid - 1
    else:
        left = mid + 1

print(last_index)