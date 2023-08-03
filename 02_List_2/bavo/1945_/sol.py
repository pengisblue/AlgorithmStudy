import sys
sys.stdin = open('input.txt')


# def get_powers(num, c):
#     cnt = 0
#     while num > 1 and num % c == 0:
#         cnt += 1
#         num //= c
#     return num, cnt
#
#
# c_list = [2,3,5,7,11]
#
# for T in range(1, int(input()) + 1):
#     result_list = []
#     number = int(input())
#     for x in c_list:
#         number, power = get_powers(number, x)
#         result_list.append(power)
#     print(f"#{T} {' '.join(map(str,result_list))}")