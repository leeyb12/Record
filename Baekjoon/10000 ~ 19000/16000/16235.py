import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 현재 양분
nutrient = [[5] * N for _ in range(N)]

# 나무 정보
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)

# 처음에 나이순 정렬
for i in range(N):
    for j in range(N):
        trees[i][j].sort()

dirs = [(-1,-1), (-1,0), (-1,1),
        (0,-1),         (0,1),
        (1,-1),  (1,0), (1,1)]

for _ in range(K):
    # 🌸 봄 + ☀ 여름
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue

            new_trees = []
            dead_nutrient = 0

            for age in trees[i][j]:
                if nutrient[i][j] >= age:
                    nutrient[i][j] -= age
                    new_trees.append(age + 1)
                else:
                    dead_nutrient += age // 2

            trees[i][j] = new_trees
            nutrient[i][j] += dead_nutrient

    # 🍂 가을
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for dx, dy in dirs:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < N:
                            trees[ni][nj].insert(0, 1)

    # ❄ 겨울
    for i in range(N):
        for j in range(N):
            nutrient[i][j] += A[i][j]

# 살아있는 나무 수 계산
result = 0
for i in range(N):
    for j in range(N):
        result += len(trees[i][j])

print(result)
