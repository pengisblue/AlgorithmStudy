N, M = map(int, input().split())

numbers = list(map(int, input().split()))


count_list = [0] * M

temp_val = 0

for i in range(N):
    temp_val = (temp_val + (numbers[i] % M)) % M
    count_list[temp_val] += 1

count_list[0] += 1
sum_of_pair = 0

for num in count_list:
    if num >= 2:
        sum_of_pair += ( num * (num - 1) ) // 2

# print(count_list)
print(sum_of_pair)