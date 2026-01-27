from collections import deque
import copy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def bfs(tmp):
    q = deque()
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))

    count = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                count += 1
    return count

def build_wall(cnt):
    global answer
    if cnt == 3:
        tmp = copy.deepcopy(board)
        answer = max(answer, bfs(tmp))
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                build_wall(cnt + 1)
                board[i][j] = 0

build_wall(0)
print(answer)
