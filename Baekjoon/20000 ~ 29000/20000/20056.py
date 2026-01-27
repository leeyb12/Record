import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# fireballs: (r, c, m, s, d)
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r-1, c-1, m, s, d))

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    grid = [[[] for _ in range(N)] for _ in range(N)]

    # 1. 이동
    for r, c, m, s, d in fireballs:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        grid[nr][nc].append((m, s, d))

    fireballs = []

    # 2. 합치기 & 분리
    for r in range(N):
        for c in range(N):
            if not grid[r][c]:
                continue

            if len(grid[r][c]) == 1:
                fireballs.append((r, c, *grid[r][c][0]))
            else:
                cnt = len(grid[r][c])
                sum_m = sum(f[0] for f in grid[r][c])
                sum_s = sum(f[1] for f in grid[r][c])
                dirs = [f[2] for f in grid[r][c]]

                nm = sum_m // 5
                if nm == 0:
                    continue

                ns = sum_s // cnt
                all_even = all(d % 2 == 0 for d in dirs)
                all_odd = all(d % 2 == 1 for d in dirs)

                if all_even or all_odd:
                    ndirs = [0, 2, 4, 6]
                else:
                    ndirs = [1, 3, 5, 7]

                for nd in ndirs:
                    fireballs.append((r, c, nm, ns, nd))

# 결과
print(sum(f[2] for f in fireballs))
