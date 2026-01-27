N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위: 위, 아래, 북, 남, 서, 동
dice = [0] * 6

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for cmd in commands:
    nx = x + dx[cmd - 1]
    ny = y + dy[cmd - 1]

    # 지도 밖이면 무시
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    # 주사위 회전
    if cmd == 1:      # 동
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif cmd == 2:    # 서
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif cmd == 3:    # 북
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    else:             # 남
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]

    # 칸과 바닥면 처리
    if board[nx][ny] == 0:
        board[nx][ny] = dice[1]
    else:
        dice[1] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])
