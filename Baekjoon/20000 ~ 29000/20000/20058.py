import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
SIZE = 2 ** N
A = [list(map(int, input().split())) for _ in range(SIZE)]
L_list = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1️⃣ 부분 격자 회전
def rotate(L):
    size = 2 ** L
    new = [[0] * SIZE for _ in range(SIZE)]

    for r in range(0, SIZE, size):
        for c in range(0, SIZE, size):
            for i in range(size):
                for j in range(size):
                    new[r + j][c + size - 1 - i] = A[r + i][c + j]
    return new

# 2️⃣ 얼음 녹이기
def melt():
    to_melt = []
    for r in range(SIZE):
        for c in range(SIZE):
            if A[r][c] == 0:
                continue
            cnt = 0
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < SIZE and 0 <= nc < SIZE and A[nr][nc] > 0:
                    cnt += 1
            if cnt < 3:
                to_melt.append((r, c))

    for r, c in to_melt:
        A[r][c] -= 1

# 3️⃣ 가장 큰 덩어리 BFS
def largest_ice():
    visited = [[False]*SIZE for _ in range(SIZE)]
    max_block = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if A[i][j] > 0 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                cnt = 1

                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < SIZE and 0 <= nc < SIZE:
                            if A[nr][nc] > 0 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                                cnt += 1

                max_block = max(max_block, cnt)
    return max_block

# 🔥 파이어스톰 실행
for L in L_list:
    if L > 0:
        A = rotate(L)
    melt()

# 결과 출력
total_ice = sum(sum(row) for row in A)
largest = largest_ice()

print(total_ice)
print(largest)
