import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기
cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)

up, down = cleaner

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    # 1️⃣ 확산
    temp = [[0] * C for _ in range(R)]
    temp[up][0] = temp[down][0] = -1

    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                spread = room[i][j] // 5
                cnt = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        temp[ni][nj] += spread
                        cnt += 1
                temp[i][j] += room[i][j] - spread * cnt

    room = temp

    # 2️⃣ 공기청정기 작동 (위쪽 - 반시계)
    for i in range(up - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    for j in range(C - 1):
        room[0][j] = room[0][j + 1]
    for i in range(up):
        room[i][C - 1] = room[i + 1][C - 1]
    for j in range(C - 1, 1, -1):
        room[up][j] = room[up][j - 1]
    room[up][1] = 0

    # 3️⃣ 공기청정기 작동 (아래쪽 - 시계)
    for i in range(down + 1, R - 1):
        room[i][0] = room[i + 1][0]
    for j in range(C - 1):
        room[R - 1][j] = room[R - 1][j + 1]
    for i in range(R - 1, down, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    for j in range(C - 1, 1, -1):
        room[down][j] = room[down][j - 1]
    room[down][1] = 0

# 결과 계산
result = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            result += room[i][j]

print(result)
