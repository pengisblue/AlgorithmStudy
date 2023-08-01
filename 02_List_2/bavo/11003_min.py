from collections import deque

d = deque()

N, L = map(int, input().split()) 

numbers = list(map(int, input().split()))

result_list = []

for i in range(L):
    d.append(numbers[i])
    if i - L + 1 > 0:
        if d.popleft() == int(result_list[-1]):
            result_list.append(str(min(d)))
        else:
            result_list.append(result_list[-1])
    else:
        result_list.append(str(min(d)))

for i in range(L, N):
    d.append(numbers[i])
    
    if d.popleft() == int(result_list[-1]):
        result_list.append(str(min(d)))
    else:
        if d[-1] < int(result_list[-1]):
            result_list.append(str(d[-1]))
        else:
            result_list.append(result_list[-1])

print(' '.join(result_list))
