import sys

sys.stdin = open('input.txt')

for T in range(1, 11):
    dump_cnt = int(input())
    boxes = list(map(int,input().split()))
    for _ in range(dump_cnt):
        boxes.sort()
        boxes[0] += 1
        boxes[-1] -= 1
    boxes.sort()
    print(f'#{T} {boxes[-1] - boxes[0]}')