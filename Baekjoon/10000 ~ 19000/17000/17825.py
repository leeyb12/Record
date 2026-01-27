n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = int(1e9)  # 기준점, 경계의 길이 정하기
total = 0
for i in range(n):
    total += sum(graph[i])

def simulate(x, y, d1, d2):
    t1, t2, t3, t4 = 0, 0, 0, 0
    check = [[0] * n for _ in range(n)]  # 경계선을 기록
    # 5번 선거구 경계선 표시하기
    # (x, y), (x+1, y-1), ..., (x+d1, y-d1)
    for i in range(d1 + 1):
        check[x+i-1][y-i-1] = 5
    # (x, y), (x+1, y+1), ..., (x+d2, y+d2)
    for i in range(d2+1):
        check[x+i-1][y+i-1] = 5
    # (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
    for i in range(d2+1):
        check[x+d1+i-1][y-d1+i-1] = 5
    # (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
    for i in range(d1+1):
        check[x+d2+i-1][y+d2-i-1] = 5

    # 경계선 만나면 break (check 칸 값이 5이면 중단)
    # 구역 1
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if check[i-1][j-1] == 5:
                break
            t1 += graph[i-1][j-1]

    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if check[i-1][j-1] == 5:
                break
            t2 += graph[i-1][j-1]

    for i in range(x+d1, n+1):
        for j in range(1, y-d1+d2):
            if check[i-1][j-1] == 5:
                break
            t3 += graph[i-1][j-1]

    for i in range(x+d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if check[i-1][j-1] == 5:
                break
            t4 += graph[i-1][j-1]

    t5 = total - (t1+t2+t3+t4)
    max_t = max(t1,t2,t3,t4,t5)
    min_t = min(t1,t2,t3,t4,t5)
    return max_t-min_t

#가능한 x, y, d1, d2의 경우의 수
for d1 in range(1, n):
    for d2 in range(1, n):
        for x in range(1, n-d1-d2+1):
            for y in range(1, n-d2+1):
                # 최솟값 갱신
                answer = min(simulate(x, y, d1, d2), answer)

print(answer)