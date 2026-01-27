import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = list(map(lambda x: x-1, map(int, input().split())))

priority = [[] for _ in range(M)]
for i in range(M):
    for _ in range(4):
        priority[i].append(list(map(lambda x: x-1, map(int, input().split()))))

# 냄새 정보: (상어 번호, 남은 시간)
smell = [[None]*N for _ in range(N)]

sharks = {}
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            s = board[i][j] - 1
            sharks[s] = [i, j, dirs[s]]
            smell[i][j] = (s, k)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0

while time <= 1000:
    if len(sharks) == 1 and 0 in sharks:
        print(time)
        exit()

    time += 1
    next_pos = {}

    # 1. 이동 방향 결정
    for s, (x, y, d) in sharks.items():
        moved = False

        # 냄새 없는 칸 탐색
        for nd in priority[s][d]:
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < N and 0 <= ny < N and smell[nx][ny] is None:
                next_pos[s] = (nx, ny, nd)
                moved = True
                break

        # 자기 냄새 있는 칸
        if not moved:
            for nd in priority[s][d]:
                nx, ny = x + dx[nd], y + dy[nd]
                if 0 <= nx < N and 0 <= ny < N:
                    if smell[nx][ny] and smell[nx][ny][0] == s:
                        next_pos[s] = (nx, ny, nd)
                        break

    # 2. 이동 및 충돌 처리
    new_board = [[-1]*N for _ in range(N)]
    new_sharks = {}

    for s in sorted(next_pos):
        x, y, d = next_pos[s]
        if new_board[x][y] == -1:
            new_board[x][y] = s
            new_sharks[s] = [x, y, d]

    sharks = new_sharks

    # 3. 냄새 감소
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                num, t = smell[i][j]
                if t-1 == 0:
                    smell[i][j] = None
                else:
                    smell[i][j] = (num, t-1)

    # 4. 새 냄새 뿌리기
    for s, (x, y, _) in sharks.items():
        smell[x][y] = (s, k)

print(-1)
