import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
answer = float('inf')

def dfs(idx, cnt):
    global answer

    # 스타트 팀이 N/2명 채워졌을 때
    if cnt == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]
        answer = min(answer, abs(start - link))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False

# 0번 사람은 항상 스타트 팀에 포함
visited[0] = True
dfs(1, 1)

print(answer)
