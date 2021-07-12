# DP스러운 그래프 탐색

import sys
sys.setrecursionlimit(10 ** 8)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 거꾸로 생각. x,y서부터 마지막 목적지까지 갈 수 있는 경로의 수
def dfs(x, y):
    # 목적지까지 탐색이 되었을 경우 : 1반환
    if x == m-1 and y == n-1:
        return 1
    # 이미 방문한 경로라면, 거기서부터는 해당 값을 반환해서 그 전 경로 시작점에 더해줌
    # 이전 좌표가 그 경로들을 흡수하게 된다(어짜피 거기서 그리로 가면 결국 똑같은거니까)
    if visited[x][y] != -1:
        return visited[x][y]
    # 방문을 했으므로 0으로 바꿈
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if a[nx][ny] < a[x][y]: # 내리막길인 경우 거기서 다시 경로탐색
                visited[x][y] += dfs(nx, ny) # 반환한 값을 더해줌(거기서부터 시작한 또다른 경로)
                #! 이 스킬 기억하자!!!!
                # 확실히 dp테이블은 거기까지 가는 모든 경로를 기록하는 것
    return visited[x][y]

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1]*n for _ in range(m)] # 초기값은 -1
print(dfs(0, 0))


'''
import sys
sys.setrecursionlimit(10 ** 8)

N, M = map(int, sys.stdin.readline().split())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1] * (M) for _ in range(N)]
dp[N - 1][M - 1] = 1

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(x, y, W, dp):
    if dp[y][x] != -1:
        return dp[y][x]

    tmp = 0
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < M and 0 <= ny < N and W[y][x] > W[ny][nx]:
            tmp += dfs(nx, ny, W, dp)
    dp[y][x] = tmp

    return dp[y][x]
print(dfs(0, 0, W, dp))
'''