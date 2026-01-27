N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0

for a in A:
    total += 1  # 총감독관 1명
    remain = a - B
    if remain > 0:
        total += (remain + C - 1) // C  # 부감독관 수

print(total)
