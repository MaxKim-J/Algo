from copy import deepcopy
from collections import deque

dr = (0,0,1,-1)
dc = (1,-1,0,0)

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = deepcopy(board)
cr, cc = map(lambda x:int(x)-1, input().split())

for _ in range(M):
  sr, sc, tr, tc = map(lambda x:int(x)-1, input().split())
  board[sr][sc] = (tr, tc)

def get_closest():
  global cr, cc, board, K
  if (board[cr][cc] != 1) and (board[cr][cc] != 0):
    board[cr][cc] = 0
    return board[cr][cc]
  visitedA = deepcopy(visited)
  queue = [(cr, cc, 0)]
  visitedA[cr][cc] = 1
  while True:
    new_queue = []
    passanger = []
    for r,c,d in queue:
      for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (-1 < nr < N) and (-1 < nc < N):
          if (visitedA[nr][nc] != 1):
            visitedA[nr][nc] = 1
            if (board[nr][nc] == 0):
              new_queue.append((nr, nc, d+1))
            else:
              passanger.append((nr, nc, d+1))

    if len(passanger) > 0:
      passanger.sort()
      r,c,d = passanger[0]
      if K - d <= 0:
        return False
      K -= d
      cr, cc = r,c
      tmp = board[r][c]
      board[r][c] = 0
      return tmp

    if len(new_queue) > 0:
      queue = new_queue[:]
    else:
      return False

def move(ahead):
  global cr, cc, board, K
  tr, tc = ahead
  visitedB = deepcopy(visited)
  queue = deque([(cr, cc, 0)])
  visitedB[cr][cc] = 1
  while queue:
    r,c,d = queue.popleft()
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if (-1 < nr < N) and (-1 < nc < N) and (visitedB[nr][nc] != 1):
        if (nr == tr) and (nc == tc):
          if K - (d+1) < 0:
            return False
          K += (d+1)
          return (nr, nc)
        visitedB[nr][nc] = 1
        queue.append((nr, nc, d+1))


for _ in range(M):
  ahead = get_closest()
  if not ahead:
    print(-1)
    exit(0)

  current = move(ahead)
  if not current:
    print(-1)
    exit(0)

  cr, cc = current[0], current[1]

print(K)

'''
import sys
from collections import deque
from heapq import heappop, heappush

n, m, f = map(int, sys.stdin.readline().rstrip().split())
arr = [[] for i in range(n)]
INF = int(1e9)
d = [[1,0], [-1,0], [0,1], [0,-1]]

for i in range(n):
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    arr[i] = x


taxi_pos = list(map(int, sys.stdin.readline().rstrip().split()))
srcs = [[] for i in range(m)]
dsts = [[] for i in range(m)]

for i in range(m):
    src_y, src_x, dst_y, dst_x = map(int, sys.stdin.readline().rstrip().split())
    srcs[i] = [src_y, src_x]
    dsts[i] = [dst_y, dst_x]

picked = [False for _ in range(m)]

def isin(y,x):
    if -1<y<n:
        if -1<x<n: return True
    return False

# 출발지와 도착지 거리 계산
def bfs():
    global taxi_pos, f
    sy, sx = taxi_pos[0] - 1, taxi_pos[1] - 1
    check = [[False for _ in range(n)] for _ in range(n)]
    table = [[INF for _ in range(n)] for _ in range(n)]
    q = deque([])
    table[sy][sx] = 0
    q.append([sy, sx])
    check[sy][sx] = True
    
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if isin(ny, nx):
                if not check[ny][nx]:
                    check[ny][nx] = True
                    if arr[ny][nx] != 1:
                        table[ny][nx] = table[y][x] + 1
                        q.append([ny, nx])
    
    return table

# 택시와 가까운 손님을 찾는 함수
def find_guest():
    global arr, f, picked 
    table = bfs()
    pq = []

    for i in range(m):
        if not picked[i]:
            y, x = srcs[i][0] - 1, srcs[i][1] - 1
            dist = table[y][x]
            if f - dist >= 0:
                heappush(pq, [dist, y, x, i]) 

    if not pq: return -1
    dist, _, _, guest_index = heappop(pq)
    f -= dist
    picked[guest_index] = True

    return guest_index

# 손님의 목적지까지 가는 함수
def go_dst(guest_index):
    global f
    table = bfs()
    y, x = dsts[guest_index][0] - 1, dsts[guest_index][1] - 1
    dist = table[y][x]
    if f - dist < 0: return -1
    return dist

# 실행코드
ok = True
cnt = m
while cnt:
    guest_index = find_guest()
    if guest_index == -1:
        ok = False
        break
    taxi_pos = srcs[guest_index]
    dist = go_dst(guest_index)
    if dist == -1:
        ok = False
        break
    f += dist
    taxi_pos = dsts[guest_index]
    cnt -= 1

if ok: print(f)
else: print(-1)
'''