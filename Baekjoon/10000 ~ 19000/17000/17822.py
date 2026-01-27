import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())
circles = [deque(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    x, d, k = map(int, input().split())

    # 1️⃣ 회전
    for i in range(x - 1, N, x):
        if d == 0:   # 시계
            circles[i].rotate(k)
        else:        # 반시계
            circles[i].rotate(-k)

    # 2️⃣ 인접한 같은 수 찾기
    remove = set()
    for i in range(N):
        for j in range(M):
            if circles[i][j] == 0:
                continue
            for d in range(4):
                ni = i + dx[d]
                nj = (j + dy[d]) % M
                if 0 <= ni < N:
                    if circles[ni][nj] == circles[i][j]:
                        remove.add((i, j))
                        remove.add((ni, nj))

    # 3️⃣ 제거 or 평균 조정
    if remove:
        for i, j in remove:
            circles[i][j] = 0
    else:
        total = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if circles[i][j] != 0:
                    total += circles[i][j]
                    cnt += 1

        if cnt == 0:
            continue

        avg = total / cnt

        for i in range(N):
            for j in range(M):
                if circles[i][j] == 0:
                    continue
                if circles[i][j] > avg:
                    circles[i][j] -= 1
                elif circles[i][j] < avg:
                    circles[i][j] += 1

# 4️⃣ 결과 출력
answer = sum(sum(circle) for circle in circles)
print(answer)
