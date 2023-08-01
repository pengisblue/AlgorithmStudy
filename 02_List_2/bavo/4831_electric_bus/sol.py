import sys

sys.stdin = open('input.txt')

def get_min_charge(distance, end, chargers):
    charge_cnt = 0

    #현위치
    curr = 0
    for i in range(len(chargers)):
        # 충전해도 못갈때
        if chargers[i] - curr > distance:
            return 0
        # 충전하면 도착할때
        if chargers[i] + distance >= end:
            charge_cnt += 1
            return charge_cnt
        # 다음정거장이 존재하고 , 충전안해도 다음 충전소까지 갈때
        if i < len(chargers) - 2 and chargers[i + 1] - curr <= distance:
            continue
        # 그냥 충전해야할때
        else:
            curr = chargers[i]
            charge_cnt += 1

# K N M
#  이동거리 총정류장개수 충전기개수

for T in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    print(f'#{T} {get_min_charge(K, N, list(map(int, input().split())))}')
