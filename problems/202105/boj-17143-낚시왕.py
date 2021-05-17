dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, 1, -1)

R, C, M = map(int, input().split())
board = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
  r,c,s,d,z = map(int, input().split())
  board[r-1][c-1].append((s,d,z))

def reverse(d):
  return d - 1 if d % 2 == 0 else d + 1

def catch(c):
  global R, board
  for r in range(R):
    if len(board[r][c]):
      shark = board[r][c].pop()
      return shark[2]
  return 0

def move():
  global R, C, board
  new_board = [[[] for _ in range(C)] for _ in range(R)]
  for r in range(R):
    for c in range(C):
      #! 여기 좀더 최적화 가능할듯 => 계산해서 바로 값을 땡기는 식으로
      if len(board[r][c]):
        s, d, z = board[r][c].pop()
        cr, cc, cs = r, c, s
        # while로 s를 하나씩 감소시키면서 한칸씩 이동시키기
        while cs > 0:
          nr, nc = cr + dr[d], cc + dc[d]
          # nr이나 nc가 겪자 밖으로 나갔을 경우(방향 바꾸고 rc에서 위치 재조정)
          if not(-1 < nr < R) or not(-1 < nc < C):
            d = reverse(d)
            nr, nc = cr + dr[d], cc + dc[d]
          cs -= 1
          cr, cc = nr, nc
        new_board[cr][cc].append((s,d,z))
  
  for r in range(R):
    for c in range(C):
      if len(new_board[r][c]) > 1:
        new_arr = [list(sorted(new_board[r][c], key=lambda x:-x[2]))[0]]
        new_board[r][c] = new_arr

  board = new_board

total = 0
# 낚시왕의 포지션 이동
for cc in range(C):
  total += catch(cc)
  move()

print(total) 

import sys

'''
#! 한칸씩 이동시키는게 아니라 계산하는 방법 => 966ms 2배 빠름

read = sys.stdin.readline
directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
r, c, m = map(int, read().strip().split())
pools = [[None for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, read().strip().split())
    pools[x - 1][y - 1] = [s, d - 1, z]
ans = 0
for fisher in range(c):

    for i in range(r):
        if pools[i][fisher]:
            ans += pools[i][fisher][2]
            pools[i][fisher] = None
            break

    nxt_sharks = []

    for x in range(r):
        for y in range(c):
            if pools[x][y]:
                s, d, z = pools[x][y]
                pools[x][y] = None
                #! 속도값을.. 무언가로 mod 해주는 모습..
                s = s % (2 * (r - 1)) if d < 2 else s % (2 * (c - 1))
                i, j = x, y
                for _ in range(s):
                    dx, dy = directions[d]
                    nx, ny = i + dx, j + dy
                    #! 격자 밖으로 나갔을때... 
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        d = 1 - d if d < 2 else 2 + (3 - d)
                    dx, dy = directions[d]
                    i, j = i + dx, j + dy
                nxt_sharks.append((i, j, s, d, z))

    for x, y, s, d, z in nxt_sharks:
        if pools[x][y]:
            if z > pools[x][y][2]:
                pools[x][y] = (s, d, z)
        else:
            pools[x][y] = (s, d, z)

print(ans)
'''