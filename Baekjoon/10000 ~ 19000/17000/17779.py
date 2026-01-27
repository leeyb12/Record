import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

INF = 10**9
answer = INF

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):

                # 범위 체크
                if x + d1 + d2 >= N:
                    continue
                if y - d1 < 0 or y + d2 >= N:
                    continue

                board = [[0] * N for _ in range(N)]

                # 5번 선거구 경계선
                for i in range(d1 + 1):
                    board[x + i][y - i] = 5
                    board[x + d2 + i][y + d2 - i] = 5

                for i in range(d2 + 1):
                    board[x + i][y + i] = 5
                    board[x + d1 + i][y - d1 + i] = 5

                # 5번 선거구 내부 채우기 (토글 방식)
                for r in range(x + 1, x + d1 + d2):
                    fill = False
                    for c in range(N):
                        if board[r][c] == 5:
                            fill = not fill
                        if fill:
                            board[r][c] = 5

                population = [0] * 5

                # 인구 계산 (5번 우선!)
                for r in range(N):
                    for c in range(N):
                        if board[r][c] == 5:
                            population[4] += A[r][c]
                        elif r < x + d1 and c <= y:
                            population[0] += A[r][c]
                        elif r <= x + d2 and c > y:
                            population[1] += A[r][c]
                        elif r >= x + d1 and c < y - d1 + d2:
                            population[2] += A[r][c]
                        else:
                            population[3] += A[r][c]

                answer = min(answer, max(population) - min(population))

print(answer)
