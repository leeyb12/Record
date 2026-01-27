from itertools import product
import sys
input = sys.stdin.readline

# 물고기 방향 (←, ↖, ↑, ↗, →, ↘, ↓, ↙)
fx = [0, -1, -1, -1, 0, 1, 1, 1]
fy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어 방향 (상, 좌, 하, 우) ← 사전순 중요
sx = [-1, 0, 1, 0]
sy = [0, -1, 0, 1]

fish = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0]*4 for _ in range(4)]

M, S = map(int, input().split())
for _ in range(M):
    x, y, d = map(int, input().split())
    fish[x-1][y-1].append(d-1)

shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1

for _ in range(S):

    # 1️⃣ 복제 저장
    copied = [[list(fish[i][j]) for j in range(4)] for i in range(4)]

    # 2️⃣ 물고기 이동
    new_fish = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for d in fish[i][j]:
                moved = False
                for k in range(8):
                    nd = (d - k) % 8
                    ni, nj = i + fx[nd], j + fy[nd]
                    if 0 <= ni < 4 and 0 <= nj < 4:
                        if smell[ni][nj] == 0 and (ni, nj) != (shark_x, shark_y):
                            new_fish[ni][nj].append(nd)
                            moved = True
                            break
                if not moved:
                    new_fish[i][j].append(d)
    fish = new_fish

    # 3️⃣ 상어 이동 (3칸)
    best = (-1, [])
    for dirs in product(range(4), repeat=3):
        x, y = shark_x, shark_y
        eaten = 0
        visited = set()
        valid = True
        for d in dirs:
            x += sx[d]
            y += sy[d]
            if not (0 <= x < 4 and 0 <= y < 4):
                valid = False
                break
            if (x, y) not in visited:
                eaten += len(fish[x][y])
                visited.add((x, y))
        if valid and eaten > best[0]:
            best = (eaten, dirs)

    # 이동 & 먹기
    x, y = shark_x, shark_y
    for d in best[1]:
        x += sx[d]
        y += sy[d]
        if fish[x][y]:
            fish[x][y] = []
            smell[x][y] = 3
    shark_x, shark_y = x, y

    # 4️⃣ 냄새 감소
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1

    # 5️⃣ 복제 완료
    for i in range(4):
        for j in range(4):
            fish[i][j].extend(copied[i][j])

# 결과
answer = sum(len(fish[i][j]) for i in range(4) for j in range(4))
print(answer)
