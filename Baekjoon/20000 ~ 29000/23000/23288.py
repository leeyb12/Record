from collections import deque
import sys
input = sys.stdin.readline

# 방향: 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 주사위 초기 상태
# top, bottom, north, south, west, east
dice = [1, 6, 2, 5, 4, 3]

def roll(d):
    top, bottom, north, south, west, east = dice
    if d == 0:      # 동
        dice[:] = [west, east, north, south, bottom, top]
    elif d == 1:    # 남
        dice[:] = [north, south, bottom, top, west, east]
    elif d == 2:    # 서
        dice[:] = [east, west, north, south, top, bottom]
    else:           # 북
        dice[:] = [south, north, top, bottom, west, east]

def bfs(x, y):
    visited = [[False]*M for _ in range(N)]
    q = deque([(x, y)])
    visited[x][y] = True
    val = board[x][y]
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny] == val:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt * val

x, y = 0, 0
dir = 0
score = 0

for _ in range(K):
    nx, ny = x + dx[dir], y + dy[dir]

    if not (0 <= nx < N and 0 <= ny < M):
        dir = (dir + 2) % 4
        nx, ny = x + dx[dir], y + dy[dir]

    roll(dir)
    x, y = nx, ny

    score += bfs(x, y)

    A = dice[1]
    B = board[x][y]

    if A > B:
        dir = (dir + 1) % 4
    elif A < B:
        dir = (dir + 3) % 4

print(score)
