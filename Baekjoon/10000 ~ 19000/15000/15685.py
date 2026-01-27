import sys
input = sys.stdin.readline

N = int(input())

# 101 x 101 격자
board = [[0] * 101 for _ in range(101)]

# 방향: → ↑ ← ↓
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, input().split())

    directions = [d]

    # 세대별 방향 생성
    for _ in range(g):
        for i in range(len(directions) - 1, -1, -1):
            directions.append((directions[i] + 1) % 4)

    # 시작점 표시
    board[y][x] = 1

    # 커브 따라 이동
    for dir in directions:
        x += dx[dir]
        y += dy[dir]
        board[y][x] = 1

# 정사각형 개수 세기
answer = 0
for y in range(100):
    for x in range(100):
        if board[y][x] and board[y+1][x] and board[y][x+1] and board[y+1][x+1]:
            answer += 1

print(answer)
