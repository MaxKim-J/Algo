#? 내풀이

'''
방향전환 수를 BFS 해보면서 세보자고 했던 아이디어는 맞고 visited에 기록하면 더 효율적으로 풀 수 있다
근데 남의풀이를 보니까 방향을 큐에 저장하지 않아도 풀린다. 방향 정보를 넣어줄 필요가 없어서 코드가 더 짧아졌다
역시... 더 숙고하고 코딩을 해야한다 최대한 있는 자료구조를 활용하자는 마음가짐으로... 열린 생각...
거의 최단경로 문제에 가까워졌다..그래도 큐 방향 어쩌구 정도만 이해하면 풀 수 있었음
'''

from collections import deque
from math import inf

dr = (-1,0,1,0)
dc = (0,1,0,-1)

def BFS(start, end, W, H):
  sr, sc = start
  er, ec = end
  visited = [[inf]*W for _ in range(H)]
  visited[sr][sc] = 0

  pre_queue = []

  for i in range(4):
    nr = sr + dr[i]
    nc = sc + dc[i]
    if -1<nr<H and -1<nc<W and board[nr][nc] == '.':
      pre_queue.append((nr, nc, i))
      visited[nr][nc] = 0

  queue = deque(pre_queue)

  while queue:
    r, c, p = queue.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if -1<nr<H and -1<nc<W and board[nr][nc] != '*':
        mirror = visited[r][c] + 1 if (p % 2 == 0 and i % 2 != 0) or (p % 2 != 0 and i % 2 == 0) else visited[r][c]
        if visited[nr][nc] > mirror:
          queue.append((nr, nc, i))
          visited[nr][nc] = mirror

  return visited

W, H = map(int, input().split())

board = []
points = []

for h in range(H):
  row = list(input())
  for r in range(W):
    if row[r] == 'C':
      points.append((h,r))
  board.append(row)

result = BFS(points[0], points[1], W, H)
print(result[points[1][0]][points[1][1]])

#* 남의풀이

from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ## 동 남 서 북 순서
            nx, ny = x + dx[i], y + dy[i]
            #! 쭉!!!!! 탐색하는 케이스 해줘보기
            while True:
                ## 범위를 벗어난다
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                ## 벽을 만난다
                if board[nx][ny] == "*":
                    break
                ##! 지난 적 있는 곳인데, 지금 경로로는 너무 많은 거울이 필요해서 break
                # 그곳에 거울을 놓는 케이스들이 다 걸러진다
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                ## board업데이트, queue 추가
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]


if __name__ == "__main__":
    ## 입력값
    m, n = map(int, input().split())
    board = [input() for _ in range(n)]

    ## 동 남 서 북
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    ## C위치
    C = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == "C":
                C.append((i, j))
    ## sx,sy : 시작지점
    ## ex,ey : 도착지점
    (sx, sy), (ex, ey) = C

    visited = [[float("inf")] * m for _ in range(n)]
    bfs(sx, sy)

    print(visited[ex][ey] - 1)