# min_max

import sys

T = int(sys.stdin.readline())

for i in range(T) :
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    max = 0
    min = float('inf')

    for a in A :
        if max < a :
            max = a
        elif min > a :
            min = a

    print(f'#{i+1} {max - min}')



