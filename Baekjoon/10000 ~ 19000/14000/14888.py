N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # +, -, *, /

max_val = -10**9
min_val = 10**9

def dfs(idx, current, plus, minus, mul, divi):
    global max_val, min_val

    if idx == N:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return

    if plus > 0:
        dfs(idx + 1, current + nums[idx],
            plus - 1, minus, mul, divi)

    if minus > 0:
        dfs(idx + 1, current - nums[idx],
            plus, minus - 1, mul, divi)

    if mul > 0:
        dfs(idx + 1, current * nums[idx],
            plus, minus, mul - 1, divi)

    if divi > 0:
        if current < 0:
            dfs(idx + 1, -(-current // nums[idx]),
                plus, minus, mul, divi - 1)
        else:
            dfs(idx + 1, current // nums[idx],
                plus, minus, mul, divi - 1)

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])

print(max_val)
print(min_val)
