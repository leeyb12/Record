N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cleaned = 0

while True:
    # 1. 현재 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2
        cleaned += 1

    found = False
    # 3. 주변 4칸 확인
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 회전
        nx = r + dx[d]
        ny = c + dy[d]

        if room[nx][ny] == 0:
            r, c = nx, ny
            found = True
            break

    # 2. 청소할 칸이 없는 경우
    if not found:
        back = (d + 2) % 4
        br = r + dx[back]
        bc = c + dy[back]

        if room[br][bc] == 1:  # 벽이면 종료
            break
        else:
            r, c = br, bc  # 후진

print(cleaned)
