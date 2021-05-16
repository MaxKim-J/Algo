from collections import deque

# 일단 순회하는 접근은 맞는데, 폭발시키는거랑 메꾸는 로직 다시 생각해보기

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]

# N, M = 7, 1

# board = [
#   [0,0,0,0,0,0,0],
#   [3,2,1,3,2,3,0],
#   [2,1,2,1,2,1,0],
#   [2,1,1,0,2,1,1],
#   [3,3,2,3,2,1,2],
#   [3,3,3,1,3,3,2],
#   [2,3,2,2,3,2,3],
# ]

# N, M = 7, 4
# board = [
#   [0,0,0,2,3,2,3],
#   [1,2,3,1,2,3,1],
#   [2,3,1,2,3,1,2],
#   [1,2,3,0,2,3,1],
#   [2,3,1,2,3,1,2],
#   [3,1,2,3,1,2,3],
#   [1,2,3,1,2,3,1],
# ]

N, M = 9, 1

board = [
  [0,0,0,0,0,0,0,0,0],
  [3,2,1,3,1,3,3,3,0],
  [1,3,3,3,1,3,3,1,0],
  [0,2,2,2,1,2,2,1,0],
  [0,1,2,1,0,2,2,1,0],
  [0,3,3,1,1,2,2,2,0],
  [0,3,3,3,1,1,1,2,0],
  [0,1,1,1,3,3,3,2,0],
  [0,0,0,0,0,0,0,0,0],
]

sr, sc = int((N+1)/2) - 1, int((N+1)/2) - 1

dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)
dd = (3, 2, 4, 1)

ans = {1:0, 2:0, 3:0}

def retrieve():
  global board, sr, sc
  r, c = sr, sc
  fwd, p = 1, 0
  blank = deque([])
  #? 한번에 촤르륵~ 할 수는 없을까 싶긴함
  while True:
    for _ in range(fwd):
      nr = r + dr[dd[p%4]]
      nc = c + dc[dd[p%4]]
      if (nr < 0) or (nc < 0):
        return
      if board[nr][nc] == 0:
        blank.append((nr, nc))
      else:
        if len(blank) > 0:
          tr, tc = blank.popleft()
          board[tr][tc], board[nr][nc] = board[nr][nc], board[tr][tc]
          blank.append((nr, nc))
      r, c = nr, nc
    p += 1
    if (p % 4 == 2) or (p % 4 == 0):
      fwd += 1

def destroy(s, d):
  global board, sr, sc
  r, c = sr, sc

  for i in range(1, s+1):
    nr = r + (dr[d] * i)
    nc = c + (dc[d] * i)
    board[nr][nc] = 0


def explode():
  global board, ans, sr, sc
  r, c = sr, sc
  fwd = 1
  p = 0
  block = []
  memo = None
  is_explode = False
  while True:
    for _ in range(fwd):
      nr = r + dr[dd[p%4]]
      nc = c + dc[dd[p%4]]

      if (nr < 0) or (nc < 0):
        return is_explode

      if not memo:
        memo = board[nr][nc]
        block.append((nr, nc))
      else:
        if memo == board[nr][nc]:
          block.append((nr, nc))
        else:
          if len(block) >= 4:
            is_explode = True
            for mr, mc in block:
              ans[memo] += 1
              board[mr][mc] = 0
          memo = board[nr][nc]
          block = [(nr, nc)]
      r, c = nr, nc

    p += 1
    if (p % 4 == 2) or (p % 4 == 0):
      fwd += 1


def reform():
  global board, sr, sc
  r, c = sr, sc
  fwd = 1
  p = 0
  group = []
  memo = None
  result = []
  while True:
    for _ in range(fwd):
      nr = r + dr[dd[p%4]]
      nc = c + dc[dd[p%4]]

      if (nr < 0) or (nc < 0):
        return result

      if not memo:
        memo = board[nr][nc]
        group.append((nr, nc))
      else:
        if memo == board[nr][nc]:
          group.append((nr, nc))
        else:
          result.append(len(group))
          result.append(memo)
          memo = board[nr][nc]
          group = [(nr, nc)]
      r, c = nr, nc

    p += 1
    if (p % 4 == 2) or (p % 4 == 0):
      fwd += 1

def refill(arr):
  global board, sr, sc
  new_board = [[0] * N for _ in range(N)]
  r, c = sr, sc
  fwd = 1
  p = 0
  while True:
    for _ in range(fwd):
      nr = r + dr[dd[p%4]]
      nc = c + dc[dd[p%4]]
      
      if (len(arr) == 0) or (nr < 0) or (nc < 0):
        board = new_board
        return

      new_board[nr][nc] = arr.pop(0)
      r, c = nr, nc
    p += 1
    if (p % 4 == 2) or (p % 4 == 0):
      fwd += 1


for m in range(M):
  s, d = map(int, input().split())
  destroy(s, d)
  retrieve()
  while True:
    is_explode = explode()
    if is_explode:
      retrieve()
    else:
      break
  refill(reform())

print(ans[1] + (ans[2]*2) + (ans[3]*3))
