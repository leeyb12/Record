import sys
input = sys.stdin.readline

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]

# 말 정보: r, c, d
horses = []
board = [[[] for _ in range(N)] for _ in range(N)]

# 방향: → ← ↑ ↓
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def reverse_dir(d):
    if d == 1: return 2
    if d == 2: return 1
    if d == 3: return 4
    return 3

for i in range(K):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    horses.append([r, c, d])
    board[r][c].append(i)

for turn in range(1, 1001):
    for i in range(K):
        r, c, d = horses[i]
        nx, ny = r + dx[d], c + dy[d]

        # 파란색 or 범위 밖
        if not (0 <= nx < N and 0 <= ny < N) or color[nx][ny] == 2:
            d = reverse_dir(d)
            horses[i][2] = d
            nx, ny = r + dx[d], c + dy[d]
            if not (0 <= nx < N and 0 <= ny < N) or color[nx][ny] == 2:
                continue

        stack = board[r][c]
        idx = stack.index(i)
        moving = stack[idx:]
        board[r][c] = stack[:idx]

        if color[nx][ny] == 1:  # 빨간색
            moving.reverse()

        board[nx][ny].extend(moving)

        for h in moving:
            horses[h][0], horses[h][1] = nx, ny

        if len(board[nx][ny]) >= 4:
            print(turn)
            sys.exit()

print(-1)
