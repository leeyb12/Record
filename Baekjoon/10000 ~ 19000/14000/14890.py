import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(line):
    used = [False] * N
    for i in range(N - 1):
        if line[i] == line[i + 1]:
            continue
        if abs(line[i] - line[i + 1]) > 1:
            return False

        # 내려감
        if line[i] - 1 == line[i + 1]:
            for j in range(i + 1, i + 1 + L):
                if j >= N or line[j] != line[i + 1] or used[j]:
                    return False
                used[j] = True

        # 올라감
        elif line[i] + 1 == line[i + 1]:
            for j in range(i, i - L, -1):
                if j < 0 or line[j] != line[i] or used[j]:
                    return False
                used[j] = True
    return True

answer = 0

# 행 검사
for i in range(N):
    if check(board[i]):
        answer += 1

# 열 검사
for j in range(N):
    col = [board[i][j] for i in range(N)]
    if check(col):
        answer += 1

print(answer)
