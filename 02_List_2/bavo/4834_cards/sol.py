import sys
sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    N = int(input())
    count_list = [0] * 10
    cards = list(map(int,input()))
    for i in range(N):
        count_list[cards[i]] += 1
    max_val = max(count_list)
    for i in range(9, -1, -1):
        if max_val == count_list[i]:
            print(f'#{T} {i} {max_val}')
            break


