import random
import time

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def generate_random_test_case(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def test_sorting_algorithm(sort_func, num_test_cases=10, max_array_size=100):
    for i in range(num_test_cases):
        size = random.randint(0, max_array_size)
        test_case = generate_random_test_case(size)
        original = test_case.copy()

        start_time = time.time()
        sort_func(test_case)
        end_time = time.time()

        execution_time_ms = (end_time - start_time) * 1000
        
        if is_sorted(test_case):
            print(f"Test case {i + 1}: PASSED | Size: {size}, Time: {execution_time_ms:.2f} ms")
        else:
            print(f"Test case {i + 1}: FAILED | Size: {size}, Time: {execution_time_ms:.2f} ms | Original: {original}, Sorted: {test_case}")