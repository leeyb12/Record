import sys
input = sys.stdin.readline

N = int(input())
students = {}
order = []

for _ in range(N * N):
    data = list(map(int, input().split()))
    students[data[0]] = set(data[1:])
    order.append(data[0])

board = [[0] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1️⃣ 자리 배치
for student in order:
    candidates = []

    for r in range(N):
        for c in range(N):
            if board[r][c] != 0:
                continue

            like_cnt = 0
            empty_cnt = 0

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] in students[student]:
                        like_cnt += 1
                    elif board[nr][nc] == 0:
                        empty_cnt += 1

            candidates.append((-like_cnt, -empty_cnt, r, c))

    candidates.sort()
    _, _, r, c = candidates[0]
    board[r][c] = student

# 2️⃣ 만족도 계산
score = [0, 1, 10, 100, 1000]
answer = 0

for r in range(N):
    for c in range(N):
        student = board[r][c]
        cnt = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] in students[student]:
                    cnt += 1
        answer += score[cnt]

print(answer)
