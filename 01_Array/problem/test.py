N = int(input())
cnt = 0
end = N
for i in range(N):
    start = i
    while range(start, end) != N:
        if sum(range(start, end)) > N:
            end -= 1
        elif sum(range(start, end)) < N:
            start += 1
    else:
        cnt += 1
print(cnt)