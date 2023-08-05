import test_sorting


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(len(arr) - 1, i - 1, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


if __name__ == '__main__':
    test_sorting.test_sorting_algorithm(bubble_sort, num_test_cases= 5, max_array_size=10)

    print('#'*50)

    test_sorting.test_sorting_algorithm(bubble_sort2, num_test_cases= 55, max_array_size=10)