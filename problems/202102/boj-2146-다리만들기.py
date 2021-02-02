'''
순회 자체를 여러번 해야하는 문제
여기서는 BFS => 같은 depth에 있는 것을 차근히 수를 올려야 하고, 최소값 문제라서
'''

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs1(x, y, cnt):
    # 섬이 몇개있는지 구하기 => visited에다가 번호로 표시하기
    q.append([x, y])
    visited[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = cnt
                    q.append([nx, ny])


def bfs2(num):
    # 여기 큐에 미리 일단 다 섬을 이루는 모든 좌표를 넣어놨음
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # * 섬의 크기를 늘려가면서 다른 섬에 닿을때까지의 거리를 구함
            if 0 <= nx < n and 0 <= ny < n:
                # * 육지를 만났는데 같은 섬인경우 == pass => 걍 pass하는 선택지도 괜찮음
                # 육지를 만났는데 다른 섬인 경우 => 먼저 작성했던 섬 구분되는 이차원 배열을 사용해서 대조
                if board[nx][ny] == 1 and visited[nx][ny] != num:
                    return visited2[x][y]-1
                # 바다를 만났고 아직 가지 않은 바다인경우 => visited가 0인 경우에만 새로 기록
                if board[nx][ny] == 0 and visited2[nx][ny] == 0:
                    # 섬의 크기를 하나씩 늘려가고 + visited에다가 기록
                    visited2[nx][ny] = visited2[x][y] + 1
                    q.append([nx, ny])


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q, q2 = deque(), deque()
cnt = 1

# visited에 섬을 번호로 표시
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visited[i][j] == 0:
            bfs1(i, j, cnt)
            cnt += 1

# 번호로 표시된 섬을 순회
ans = sys.maxsize
for k in range(1, cnt):
    q = deque()
    visited2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and visited[i][j] == k:
                # 큐에다가 미리! 섬을 구성하는 모든 1칸들을 다 넣어놓음
                q.append([i, j])
                # 지금 현재 순회하는 섬을 1로 만듬 => 거기서부터 시작
                visited2[i][j] = 1
    res = bfs2(k)
    ans = min(ans, res)
print(ans)
# 섬들을 먼저 순회한뒤 말단에서 그 다음에 다른 섬들로 출발하고 섬을 만났을때
