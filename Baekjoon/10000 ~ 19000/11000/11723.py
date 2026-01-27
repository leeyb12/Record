import sys
input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    cmd = input().split()

    if cmd[0] == "add":
        x = int(cmd[1])
        S |= (1 << x)

    elif cmd[0] == "remove":
        x = int(cmd[1])
        S &= ~(1 << x)

    elif cmd[0] == "check":
        x = int(cmd[1])
        print(1 if S & (1 << x) else 0)

    elif cmd[0] == "toggle":
        x = int(cmd[1])
        S ^= (1 << x)

    elif cmd[0] == "all":
        S = (1 << 21) - 1

    elif cmd[0] == "empty":
        S = 0
