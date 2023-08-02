# 1427 _ 소트인사이드
import sys

n_list = list(map(int, input()))
n_list.sort(reverse=True)

print(*n_list, sep='')