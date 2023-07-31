def count_sum_of_two_elements(nums):
    global n
    good_count = 0

    for i in range(n):
        left, right = 0, n - 1

        # 왼쪽 포인터가 오른쪽 포인터를 넘을때까지
        while left < right:
            if left == i:  # 왼쪽 포인터가 자신일땐 넘어가기
                left += 1
            elif right == i: # 오른쪽 포인터가 자신일땐 넘어가기
                right -= 1
            else:
                total = nums[left] + nums[right]

                if total == nums[i]:  # 합이 자신의 값과 같으면 카운트하고 break
                    good_count += 1
                    break
                elif total < nums[i]:  # 합이 자신의 값보다 작으면 왼쪽 포인터 한칸 오른쪽
                    left += 1
                else:  # 합이 자신의 값보다 크면 오른쪽 포인터 한칸 왼쪽
                    right -= 1

    return good_count


n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

result = count_sum_of_two_elements(numbers)
print(result)
