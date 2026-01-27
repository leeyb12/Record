import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
answer = 0

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, total):
    global answer
    if depth == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

# ㅗ 모양 처리
def check_t(x, y):
    global answer
    for i in range(4):
        temp = board[x][y]
        for j in range(3):
            k = (i + j) % 4
            nx = x + dx[k]
            ny = y + dy[k]
            if not (0 <= nx < N and 0 <= ny < M):
                break
            temp += board[nx][ny]
        else:
            answer = max(answer, temp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_t(i, j)

print(answer)
