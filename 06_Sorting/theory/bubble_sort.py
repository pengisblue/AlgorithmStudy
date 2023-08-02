import test_sorting

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



test_sorting.test_sorting_algorithm(bubble_sort, num_test_cases= 50, max_array_size=2000)