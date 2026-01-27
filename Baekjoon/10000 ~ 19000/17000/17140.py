from collections import Counter

def sort_line(line):
    counter = Counter(line)
    if 0 in counter:
        del counter[0]

    items = sorted(counter.items(), key=lambda x: (x[1], x[0]))

    result = []
    for num, cnt in items:
        result.extend([num, cnt])

    return result[:100]


def r_operation(A):
    new_A = []
    max_len = 0

    for row in A:
        sorted_row = sort_line(row)
        new_A.append(sorted_row)
        max_len = max(max_len, len(sorted_row))

    for row in new_A:
        row.extend([0] * (max_len - len(row)))

    return new_A


def c_operation(A):
    A = list(zip(*A))  # transpose
    A = r_operation([list(row) for row in A])
    return list(map(list, zip(*A)))  # transpose back


def solve():
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1

    A = [list(map(int, input().split())) for _ in range(3)]

    for time in range(101):
        if r < len(A) and c < len(A[0]) and A[r][c] == k:
            print(time)
            return

        if len(A) >= len(A[0]):
            A = r_operation(A)
        else:
            A = c_operation(A)

    print(-1)


solve()
