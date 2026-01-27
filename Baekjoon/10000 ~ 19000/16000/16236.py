import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            sx, sy = i, j
            space[i][j] = 0

size = 2
eat = 0
time = 0

dx = [-1, 0, 0, 1]  # 위, 왼, 오, 아래
dy = [0, -1, 1, 0]

def bfs(x, y, size):
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    fishes = []
    min_dist = None

    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if space[nx][ny] <= size:
                    visited[nx][ny] = visited[cx][cy] + 1
                    dist = visited[nx][ny]

                    if min_dist is not None and dist > min_dist:
                        continue

                    if 0 < space[nx][ny] < size:
                        fishes.append((dist, nx, ny))
                        min_dist = dist

                    q.append((nx, ny))

    return fishes

while True:
    fishes = bfs(sx, sy, size)
    if not fishes:
        break

    fishes.sort()  # 거리 → 위 → 왼
    dist, nx, ny = fishes[0]

    time += dist
    sx, sy = nx, ny
    space[nx][ny] = 0

    eat += 1
    if eat == size:
        size += 1
        eat = 0

print(time)
