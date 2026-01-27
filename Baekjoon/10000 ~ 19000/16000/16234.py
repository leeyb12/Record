import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

days = 0

while True:
    visited = [[False] * N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue

            q = deque()
            q.append((i, j))
            visited[i][j] = True
            union = [(i, j)]
            total = A[i][j]

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        if L <= abs(A[x][y] - A[nx][ny]) <= R:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            union.append((nx, ny))
                            total += A[nx][ny]

            if len(union) > 1:
                moved = True
                avg = total // len(union)
                for x, y in union:
                    A[x][y] = avg

    if not moved:
        break

    days += 1

print(days)
