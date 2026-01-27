n = int(input())
channels = [input().strip() for _ in range(n)]

result = []
cursor = 0

# 1️⃣ KBS1을 맨 위로
idx1 = channels.index("KBS1")

# 화살표 이동
while cursor < idx1:
    result.append("1")
    cursor += 1

# KBS1을 위로 끌어올림
while idx1 > 0:
    result.append("4")
    channels[idx1], channels[idx1 - 1] = channels[idx1 - 1], channels[idx1]
    idx1 -= 1
    cursor -= 1

# 2️⃣ KBS2를 두 번째로
idx2 = channels.index("KBS2")

# 화살표 이동
while cursor < idx2:
    result.append("1")
    cursor += 1

# KBS2를 두 번째로
while idx2 > 1:
    result.append("4")
    channels[idx2], channels[idx2 - 1] = channels[idx2 - 1], channels[idx2]
    idx2 -= 1
    cursor -= 1

print("".join(result))
