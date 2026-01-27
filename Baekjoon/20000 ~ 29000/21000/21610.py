import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 방향: ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 방향 (물복사버그)
diag = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

# 초기 구름
clouds = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1  # 0-index

    # 1. 구름 이동
    moved = set()
    for r, c in clouds:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        moved.add((nr, nc))

    # 2. 비 내리기
    for r, c in moved:
        A[r][c] += 1

    # 3. 물복사버그
    for r, c in moved:
        cnt = 0
        for drc, dcc in diag:
            nr, nc = r + drc, c + dcc
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0:
                cnt += 1
        A[r][c] += cnt

    # 4. 새 구름 생성
    new_clouds = set()
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and (i, j) not in moved:
                A[i][j] -= 2
                new_clouds.add((i, j))

    clouds = new_clouds

# 결과 출력
print(sum(map(sum, A)))
