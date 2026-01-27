import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, color, visited):
    q = deque([(sr, sc)])
    blocks = [(sr, sc)]
    rainbow = []
    visited[sr][sc] = True
    rainbow_cnt = 0

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if board[nr][nc] == color or board[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    blocks.append((nr, nc))
                    if board[nr][nc] == 0:
                        rainbow.append((nr, nc))
                        rainbow_cnt += 1

    # 무지개 방문 초기화
    for r, c in rainbow:
        visited[r][c] = False

    # 기준 블록
    normal = [(r, c) for r, c in blocks if board[r][c] > 0]
    normal.sort()
    base_r, base_c = normal[0]

    return (len(blocks), rainbow_cnt, base_r, base_c, blocks)

def apply_gravity():
    for c in range(N):
        for r in range(N-1, -1, -1):
            if board[r][c] == -2:
                nr = r - 1
                while nr >= 0 and board[nr][c] == -2:
                    nr -= 1
                if nr < 0 or board[nr][c] == -1:
                    continue
                board[r][c], board[nr][c] = board[nr][c], -2

def rotate():
    global board
    board = [list(row) for row in zip(*board)][::-1]

score = 0

while True:
    visited = [[False]*N for _ in range(N)]
    groups = []

    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                g = bfs(i, j, board[i][j], visited)
                if g[0] >= 2:
                    groups.append(g)

    if not groups:
        break

    groups.sort(reverse=True)
    size, _, _, _, blocks = groups[0]

    score += size * size
    for r, c in blocks:
        board[r][c] = -2

    apply_gravity()
    rotate()
    apply_gravity()

print(score)
