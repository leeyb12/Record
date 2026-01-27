import copy
import sys
input = sys.stdin.readline

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

board = [[None]*4 for _ in range(4)]
fish_pos = {}

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        num = data[j*2]
        d = data[j*2+1] - 1
        board[i][j] = [num, d]
        fish_pos[num] = (i, j)

answer = 0

def move_fish(board, fish_pos, sx, sy):
    for f in range(1, 17):
        if f not in fish_pos:
            continue
        x, y = fish_pos[f]
        d = board[x][y][1]

        for _ in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                if board[nx][ny]:
                    other = board[nx][ny][0]
                    board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                    fish_pos[f] = (nx, ny)
                    fish_pos[other] = (x, y)
                else:
                    board[nx][ny] = board[x][y]
                    board[x][y] = None
                    fish_pos[f] = (nx, ny)
                board[nx][ny][1] = d
                break
            d = (d + 1) % 8

def dfs(board, fish_pos, sx, sy, sdir, total):
    global answer
    answer = max(answer, total)

    move_fish(board, fish_pos, sx, sy)

    for step in range(1, 4):
        nx = sx + dx[sdir] * step
        ny = sy + dy[sdir] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny]:
            new_board = copy.deepcopy(board)
            new_fish = copy.deepcopy(fish_pos)

            fish_num, fish_dir = new_board[nx][ny]
            del new_fish[fish_num]
            new_board[nx][ny] = None

            dfs(new_board, new_fish, nx, ny, fish_dir, total + fish_num)

# 시작
start_fish, start_dir = board[0][0]
del fish_pos[start_fish]
board[0][0] = None

dfs(board, fish_pos, 0, 0, start_dir, start_fish)

print(answer)
