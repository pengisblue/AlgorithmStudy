import test_sorting


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


def selection_sort2(arr):
    n = len(arr)

    for i in range(n - 1 , -1, - 1):
        max_idx = i
        for j in range(i - 1, -1, -1):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[max_idx], arr[i] = arr[i], arr[max_idx]


if __name__ == '__main__':
    test_sorting.test_sorting_algorithm(selection_sort, num_test_cases = 50, max_array_size = 200)
    print('#' * 50)
    test_sorting.test_sorting_algorithm(selection_sort2, num_test_cases=50, max_array_size=200)
