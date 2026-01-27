import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

# 좌표 분리
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

answer = float('inf')

# 치킨집 M개 선택
for selected in combinations(chickens, M):
    total = 0
    for hx, hy in houses:
        dist = min(abs(hx - cx) + abs(hy - cy) for cx, cy in selected)
        total += dist
    answer = min(answer, total)

print(answer)
