import sys
input = sys.stdin.readline

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]

cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j, office[i][j]))

cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def watch(board, x, y, dirs):
    for d in dirs:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = '#'

def dfs(idx, board):
    global answer
    if idx == len(cctvs):
        count = sum(row.count(0) for row in board)
        answer = min(answer, count)
        return

    x, y, t = cctvs[idx]
    for dirs in cctv_dir[t]:
        new_board = [row[:] for row in board]
        watch(new_board, x, y, dirs)
        dfs(idx + 1, new_board)

answer = float('inf')
dfs(0, office)
print(answer)
