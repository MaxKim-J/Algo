from collections import deque

N, L, R = map(int, input().split())
board = []

for _ in range(N):
  board.append(list(map(int, input().split())))

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def BFS(sr, sc, visited):
  global board, flag, L, R, N
  nation = [(sr, sc)]
  total = board[sr][sc]
  count = 1
  queue = deque([(sr, sc)])
  visited[sr][sc] = 1

  while queue:
    r, c = queue.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if (-1 < nr < N) and (-1 < nc < N) and (visited[nr][nc] == 0):
        if L <= abs(board[r][c] - board[nr][nc]) <= R:
          total += board[nr][nc]
          count += 1
          nation.append((nr, nc))
          queue.append((nr, nc))
          visited[nr][nc] = 1

  return (total//count, nation) # 이거 그냥 nation만 리턴하면 그 값 토대로 count와 total은 다 구할 수 있음

result = 0

while True:
  flag = False
  visited = [[0] * N for _ in range(N)]

  nations = []

  for r in range(N):
    for c in range(N):
      if visited[r][c] == 0:
        total, nation = BFS(r, c, visited)
        if len(nation) > 1:
          nations.append((total, nation))

  for total, nation in nations:
    for r, c in nation:
      board[r][c] = total
      flag = True

  if flag == True:
    result += 1
  else:
    break

print(result)