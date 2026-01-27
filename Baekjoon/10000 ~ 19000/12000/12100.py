import copy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def move(board, direction):
    new_board = [[0] * N for _ in range(N)]

    for i in range(N):
        temp = []
        for j in range(N):
            if direction == 0:      # 상
                if board[j][i]:
                    temp.append(board[j][i])
            elif direction == 1:    # 하
                if board[N-1-j][i]:
                    temp.append(board[N-1-j][i])
            elif direction == 2:    # 좌
                if board[i][j]:
                    temp.append(board[i][j])
            else:                   # 우
                if board[i][N-1-j]:
                    temp.append(board[i][N-1-j])

        idx = 0
        while idx < len(temp):
            if idx + 1 < len(temp) and temp[idx] == temp[idx + 1]:
                temp[idx] *= 2
                temp.pop(idx + 1)
            idx += 1

        for j in range(len(temp)):
            if direction == 0:
                new_board[j][i] = temp[j]
            elif direction == 1:
                new_board[N-1-j][i] = temp[j]
            elif direction == 2:
                new_board[i][j] = temp[j]
            else:
                new_board[i][N-1-j] = temp[j]

    return new_board

def dfs(board, depth):
    global answer
    if depth == 5:
        for row in board:
            answer = max(answer, max(row))
        return

    for d in range(4):
        dfs(move(board, d), depth + 1)

dfs(board, 0)
print(answer)
