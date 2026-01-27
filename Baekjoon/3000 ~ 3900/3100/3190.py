from collections import deque

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

# 사과 위치
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2

L = int(input())
turns = {}
for _ in range(L):
    t, d = input().split()
    turns[int(t)] = d

# 방향: 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque()
snake.append((0, 0))
board[0][0] = 1

direction = 0
time = 0
x, y = 0, 0

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽 또는 자기 몸 충돌
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1:
        print(time)
        break

    # 이동
    snake.append((nx, ny))

    if board[nx][ny] == 2:  # 사과
        board[nx][ny] = 1
    else:  # 사과 없음
        tx, ty = snake.popleft()
        board[tx][ty] = 0
        board[nx][ny] = 1

    x, y = nx, ny

    # 방향 전환
    if time in turns:
        if turns[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
