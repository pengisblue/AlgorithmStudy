N = int(input())
scores = list(map(int, input().split()))
M = scores[0]  # 최댓값
scores_sum = 0  # 점수 합
for score in scores:
    if M < score:
        M = score
    scores_sum += score

average = (scores_sum / M * 100) / N
print(average)

# M = max(scores)
# scores_sum = sum(scores)
# av = (scores_sum / M * 100) / N
