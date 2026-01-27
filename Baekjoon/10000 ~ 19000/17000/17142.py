from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

viruses = []
empty_count = 0

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            viruses.append((i, j))
        elif lab[i][j] == 0:
            empty_count += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = 10**9
answer = INF


def bfs(active):
    visited = [[-1]*N for _ in range(N)]
    q = deque()

    for x, y in active:
        visited[x][y] = 0
        q.append((x, y))

    spread = 0
    time = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    if lab[nx][ny] == 0:
                        spread += 1
                        time = visited[nx][ny]

    if spread == empty_count:
        return time
    return INF


for active in combinations(viruses, M):
    answer = min(answer, bfs(active))

print(answer if answer != INF else -1)
