N = int(input())
cnt = 1
start = end = total = 1

while end <= N//2+1 and end != N:  # 절반보다 커지면 합으로 나타낼 수 없음
    if total == N:
        cnt += 1
        end += 1
        total += end
    elif total < N:
        end += 1
        total += end
    else:
        total -= start
        start += 1

print(cnt)





# prefix = [0]  # 합배열
# sum_n = 0  # 1 ~ n 까지의 합
# cnt = 1  # 가지수, 자기 자신을 추가해서 1
# for i in range(1, N//2+2):  # 절반보다 커지면 합으로 나타낼 수 없음
#     sum_n += i
#     prefix.append(sum_n)
#
# i_idx = 0  # 합배열이 N보다 커지기 시작하는 위치 == 구간합 순회 시작 위치
# while prefix[i_idx] < N:  # prefix[n_idx] >= N 때의 n_idx
#     i_idx += 1
#
# k = 0
# for i in range(i_idx, N//2+2):
#     for j in range(k, i):
#         if prefix[i] - prefix[j] == N:
#             cnt += 1
#             break
#     k += 1
#
# print(cnt)
#
