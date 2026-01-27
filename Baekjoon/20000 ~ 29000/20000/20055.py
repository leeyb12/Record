import sys
input = sys.stdin.readline

N, K = map(int, input().split())
durability = list(map(int, input().split()))
robot = [False] * N

step = 0

while True:
    step += 1

    # 1. 벨트 회전
    durability = [durability[-1]] + durability[:-1]
    robot = [False] + robot[:-1]
    robot[N-1] = False  # 내리는 위치 로봇 제거

    # 2. 로봇 이동
    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i+1] and durability[i+1] > 0:
            robot[i] = False
            robot[i+1] = True
            durability[i+1] -= 1

    robot[N-1] = False  # 이동 후 내리는 위치 제거

    # 3. 로봇 올리기
    if durability[0] > 0:
        robot[0] = True
        durability[0] -= 1

    # 4. 종료 조건
    if durability.count(0) >= K:
        print(step)
        break
