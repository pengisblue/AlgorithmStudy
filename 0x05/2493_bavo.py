N = int(input())

towers = list(map(int,input().split()))

# 더미 (필요없는거같음)
compare_tower = [{'height':0, 'index':0}]

result = []

for i in range(N):
    # 타워 추가하기전에 먼저 주파수를 쏴서 닿는 타워 있는지 찾아보기
    for j in range(len(compare_tower) -1, -1, -1):
        if compare_tower[j]['height'] > towers[i]:
            # 닿는 타워 있으면 해당 타워의 인덱스를 결과값에 추가
            result.append(compare_tower[j]['index'])
            break
    else:
        # 비교용 타워 다 순회했는데 자기보다 높은 타워가 없으면 0임
        result.append(0)
    
    # 스택은 내림차순 형태로 존재해야함 9 7 6 4
    # 비교용 타워가 비었을때 -1이 없어서 인덱스 오류남
    while len(compare_tower) > 0 and compare_tower[-1]['height'] <= towers[i]:
        # 자기보다 높은 타워 나올때까지 pop해주기(같은 높이도 죽여야함)
        compare_tower.pop()
    
    # 새로 발견한 타워는 무조건 저장됨
    # 비교용타워에는 자기보다 높은 타워가 내림차순으로 정렬되어있음(없으면 비어있음)
    new_compare = {'height':towers[i], 'index':i+1}
    compare_tower.append(new_compare)

print(' '.join(map(str,result)))

