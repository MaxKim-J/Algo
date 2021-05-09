from collections import deque
from copy import deepcopy

'''
2**N이 N이 아니어서 처음에 참조실수를 했음. 이런거는 처음부터 따른 변수로 선언하기
얼음이 0인거 예외처리 해줬어야 했는데 까먹어서 지체되었음
'''

dr = (0,0,1,-1)
dc = (1,-1,0,0)

N, Q = map(int, input().split())
n = 2**N

board = [list(map(int, input().split())) for _ in range(n)]
steps = list(map(int, input().split()))

def fire_storm(step):
  global board
  # 격자로 나눠서 90도 돌리기
  step_limit = 2**step
  new_board = deepcopy(board)
  for cr in range(0, n, step_limit):
    for cc in range(0, n, step_limit):
      for ar in range(step_limit):
        for ac in range(step_limit):
          hr = cr + ar
          hc = cc + ac
          new_board[cr+ac][(cc + step_limit-1) -ar] = board[hr][hc]

  board = new_board
  new_new_board = deepcopy(board)

  # 완전탐색으로 얼음 줄이기
  for r in range(n):
    for c in range(n):
      if board[r][c] > 0:
        ice = 0
        for i in range(4):
          nr = r + dr[i]
          nc = c + dc[i]
          if (-1 < nr < n) and (-1 < nc < n) and (board[nr][nc] != 0):
            ice += 1
        if ice < 3 :
          new_new_board[r][c] -= 1

  board = new_new_board

for i in range(Q):
  fire_storm(steps[i])

def BFS(sr, sc, visited):
  queue = deque([(sr, sc)])
  visited[sr][sc] = 1
  chunk = 1
  while queue:
    r, c = queue.popleft()
    for i in range(4):
      nr = dr[i] + r
      nc = dc[i] + c
      if (-1 < nr < n) and (-1 < nc < n) and (visited[nr][nc] == 0):
        if board[nr][nc] != 0:
          visited[nr][nc] = 1
          queue.append((nr, nc))
          chunk += 1
  return chunk

visited = [[0] * (n) for _ in range(n)]
max_chunk = 0

for r in range(n):
  for c in range(n):
    if (visited[r][c] == 0) and (board[r][c] > 0):
      max_chunk = max(BFS(r,c,visited), max_chunk)

total = 0

for i in range(n):
  total += sum(board[i])

print(total)
print(max_chunk)