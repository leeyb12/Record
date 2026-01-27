import sys
input = sys.stdin.readline

def rotate(gear, direction):
    if direction == 1:      # 시계
        return [gear[-1]] + gear[:-1]
    else:                   # 반시계
        return gear[1:] + [gear[0]]

gears = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())

for _ in range(K):
    num, dir = map(int, input().split())
    num -= 1

    rotate_dir = [0] * 4
    rotate_dir[num] = dir

    # 왼쪽 전파
    for i in range(num, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rotate_dir[i - 1] = -rotate_dir[i]
        else:
            break

    # 오른쪽 전파
    for i in range(num, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotate_dir[i + 1] = -rotate_dir[i]
        else:
            break

    # 실제 회전
    for i in range(4):
        if rotate_dir[i] != 0:
            gears[i] = rotate(gears[i], rotate_dir[i])

# 점수 계산
score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += (1 << i)

print(score)
