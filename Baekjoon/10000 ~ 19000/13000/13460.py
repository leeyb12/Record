from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

visited = set()
visited.add((rx, ry, bx, by))
q = deque()
q.append((rx, ry, bx, by, 0))

while q:
    rx, ry, bx, by, depth = q.popleft()

    if depth >= 10:
        break

    for i in range(4):
        nrx, nry, rc = move(rx, ry, dx[i], dy[i])
        nbx, nby, bc = move(bx, by, dx[i], dy[i])

        # 파란 구슬이 빠지면 실패
        if board[nbx][nby] == 'O':
            continue

        # 빨간 구슬만 빠지면 성공
        if board[nrx][nry] == 'O':
            print(depth + 1)
            exit()

        # 겹치는 경우 처리
        if nrx == nbx and nry == nby:
            if rc > bc:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]

        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, depth + 1))

print(-1)
