# n = 8
# video = [
#     ['1', '1', '1', '1', '0', '0', '0', '0'],
#     ['1', '1', '1', '1', '0', '0', '0', '0'],
#     ['0', '0', '0', '1', '1', '1', '0', '0'],
#     ['0', '0', '0', '1', '1', '1', '0', '0'],
#     ['1', '1', '1', '1', '0', '0', '0', '0'],
#     ['1', '1', '1', '1', '0', '0', '0', '0'],
#     ['1', '1', '1', '1', '0', '0', '1', '1'],
#     ['1', '1', '1', '1', '0', '0', '1', '1'],
# ]

n = int(input())
video = [list(input()) for i in range(n)]


def solve(R, C, W):
    global result
    should_be = video[R][C]
    for r in range(R, R+W):
        for c in range(C, C+W):
            if (video[r][c] != should_be):
                result += '('
                for i in range(2):
                    for j in range(2):
                        solve(R + i*(W//2), C + j*(W//2), W//2)
                result += ')'
                return
    result += should_be


result = ''

solve(0, 0, n)
print(result)
