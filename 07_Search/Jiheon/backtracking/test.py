
sdoku = []
for _ in range(9):
    sdoku.append(list(map(int, input().split())))

blank = []
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            blank.append([i, j])

def checkrow(x, a):
    for i in range(9):
        if a == sdoku[x][i]:
            return 0
    return 1

def checkcol(y, a):
    for i in range(9):
        if a == sdoku[i][y]:
            return 0
    return 1

def checkbox(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == sdoku[nx+i][ny+j]:
                return 0
    return 1

def dfs(i):
        if i == len(blank):
            for j in range(9):
                print(*sdoku[j])
            return 0
            
        x, y = blank[i]
        for a in range(1, 10):
            if checkrow(x, a) and checkcol(y, a) and checkbox(x, y, a):
                sdoku[x][y] = a
                dfs(i + 1)
                sdoku[x][y] = 0

dfs(0)