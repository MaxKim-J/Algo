from collections import deque
from copy import deepcopy
from itertools import permutations

dr = (0,0,1,-1)
dc = (1,-1,0,0)

def BFS(start, board, target, w, h):
  global new_start_points, new_answer
  queue = deque([(start, 0)])
  visited = [[0]*w for _ in range(h)]
  visited[start[0]][start[1]] = -1
  while queue:
    pos, depth = queue.popleft()
    r, c = pos
    if board[r][c] == '*' and (r,c) == target:
      return depth
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if -1 < nr < h and -1 < nc < w:
        if board[nr][nc] != 'x' and visited[nr][nc] == 0:
          queue.append(((nr,nc), depth+1))
          visited[nr][nc] = -1
  return -1

while True:
  w, h = map(int, input().split())
  
  if w == 0 and h == 0:
    break

  start = None
  dirty_points = []
  board = []

  for i in range(h):
    row = list(input())
    for j in range(w):
      if row[j] == '*':
        dirty_points.append((i,j))
      if row[j] == 'o':
        start = (i,j)
    board.append(row)

  visit_order =list(permutations(dirty_points, len(dirty_points)))

  answer = []

  for order in visit_order:
    total_cost = 0
    new_board = deepcopy(board)
    start_point = start

    for pos in order:
      sr, sc = start_point
      new_board[sr][sc] = '.'
      cost = BFS(start_point, new_board, pos, w, h)
      if cost == -1:
        answer = -1
        break
      else:
        start_point = pos
        total_cost += cost

    if answer == -1:
      break
    else:
      answer.append(total_cost)

  print(min(answer) if answer != -1 else -1)


# 중요한건 그게 정말 최소냐! 그렇게 픽하는게 진짜 최소를 보장하냐! 의심해볼것