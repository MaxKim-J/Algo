# 으아 너무 어렵다..............BFS보다 시간을 줄여야만 돌아가는듯????
# BFS: 시간초과
# DFS: 런타임에러

# 이거 리팩토링
import sys
sys.setrecursionlimit(10**9)


def solve(i, j, depth):
    if visit[i][j][depth] >= 0:
        return visit[i][j][depth]

    if table[i][j] != target[depth]:
        visit[i][j][depth] = 0
        return 0

    depth += 1
    if depth == len_target:
        visit[i][j][depth-1] = 1
        return 1

    cnt = 0
    for t in range(-k, k+1):
        if t == 0:
            continue

        it, jt = i+t, j+t
        if 0 <= it < n:
            cnt += solve(it, j, depth)
        if 0 <= jt < m:
            cnt += solve(i, jt, depth)
    visit[i][j][depth-1] = cnt
    return cnt


n, m, k = map(int, sys.stdin.readline().split())
table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
target = sys.stdin.readline().rstrip()
len_target = len(target)

visit = [[[-1]*len_target for j in range(m)] for i in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if table[i][j] == target[0]:
            ans += solve(i, j, 0)
print(ans)


'''
내풀이...(시간초과)

N, M, K = map(int, input().split())
board = ''
for _ in range(M):
    board += input()
target = input()


def enable_node(index):
    result = []
    Y = index % N
    X = index // M

    for i in range(K):
        north, south, west, east = Y+(i+1), Y-(i+1), X-(i+1), X+(i+1)
        if -1 < west < N:
            result.append(west * M + Y)
        if -1 < east < N:
            result.append(east * M + Y)
        if -1 < north < M:
            result.append(X * M + north)
        if -1 < south < M:
            result.append(X * M + south)
    return result


def DFS(start, target):
    count = 0
    stack = [(start, 0, target[0])]
    depth_limit = len(target) - 1
    while stack:
        visit, depth, path = stack.pop()
        if path == target:
            count += 1
        for idx in enable_node(visit):
            if (depth < depth_limit) and (target[depth + 1] == board[idx]):
                stack.append((idx, depth + 1, path+board[idx]))
    return count


# 시작점이 되는 후보 설정
start = [i for i, elem in enumerate(board) if elem == target[0]]
result = 0
for num in start:
    result += DFS(num, target)

print(result)
'''
