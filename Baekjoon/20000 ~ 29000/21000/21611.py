from sys import stdin


n, m, d, s = 0, 0, 0, 0
marbles = []
board = []
coors = {}
score = 0


def init_board() -> None:
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    cur = n ** 2 - 1
    row, col = 0, 0

    for i in range((n - 1) // 2, 0, -1):
        for j in range(4):
            for k in range(i * 2):
                coors[cur] = (row, col)
                cur -= 1
                row += dy[j]
                col += dx[j]

        row += 1
        col += 1


def fill_blanks() -> None:
    cur = 1
    target = cur
    while cur < n ** 2 and target < n ** 2:
        cy, cx = coors[cur]
        ny, nx = coors[target]
        while target < n ** 2 - 1 and marbles[ny][nx] == 0:
            target += 1
            ny, nx = coors[target]

        marbles[cy][cx] = marbles[ny][nx]

        cur += 1
        target += 1

    for i in range(n ** 2 - (target - cur), n ** 2):
        cy, cx = coors[i]
        marbles[cy][cx] = 0


def explode_marbles() -> bool:
    global score

    res = False
    i = 1
    while i < n ** 2:
        cur, cnt = i, 0
        cy, cx = coors[cur]
        marble = marbles[cy][cx]
        if marble == 0:
            break
        ny, nx = cy, cx
        while marbles[ny][nx] == marble:
            cnt += 1
            cur += 1
            ny, nx = coors[cur]
        if cnt >= 4:
            for j in range(cur - cnt, cur):
                ny, nx = coors[j]
                marbles[ny][nx] = 0

            score += marble * cnt
            fill_blanks()
            res = True
            continue
        i += 1

    return res


def group_marbles() -> None:
    global marbles

    new_marbles = [[0] * n for _ in range(n)]
    i = cur = 1
    cy, cx = coors[i]
    ay, ax = cy, cx
    while i < n ** 2 - 1 and marbles[ay][ax] != 0:
        cnt = 0
        target = cur
        by, bx = coors[target]
        marble = marbles[ay][ax]
        while target < n ** 2 - 1 and marbles[by][bx] == marble:
            cnt += 1
            target += 1
            by, bx = coors[target]

        ay, ax = by, bx
        cur = target
        cy, cx = coors[i]
        new_marbles[cy][cx] = cnt
        cy, cx = coors[i + 1]
        new_marbles[cy][cx] = marble
        i += 2

    marbles[:] = new_marbles[:]


def blizzard() -> None:
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]
    center = n // 2

    # 블리자드 -> 구슬 파괴 -> 빈칸 채우기
    for i in range(1, s + 1):
        ny, nx = center + (dy[d] * i), center + (dx[d] * i)
        marbles[ny][nx] = 0
    fill_blanks()

    # 4연속 구슬 파괴
    while explode_marbles():
        continue

    # 그룹화
    group_marbles()


if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    for _ in range(n):
        marbles.append(list(map(int, stdin.readline().split())))

    init_board()

    for _ in range(m):
        d, s = map(int, stdin.readline().split())
        blizzard()

    print(score)