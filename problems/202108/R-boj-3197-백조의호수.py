from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2: # 다른 백조 위치까지 갔다면 끝
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not c[nx][ny]:
                    if a[nx][ny] == '.':
                        q.append([nx, ny])
                    else: # 얼음일 경우
                        q_temp.append([nx, ny]) # 다음에 순회할 것들을 미리 넣는다(답이 안나왔으면 바꿔치기)
                    c[nx][ny] = 1 # 백조 visited 이미 했음
    return 0

# 이건 그냥 일반적인 BFS
def melt():
    while wq:
        x, y = wq.popleft()
        if a[x][y] == 'X':
            a[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not wc[nx][ny]:
                    if a[nx][ny] == 'X':
                        wq_temp.append([nx, ny]) # 역시 다음에 물이 될 친구들을 넣는다
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1 # 이미 방문함

m, n = map(int, input().split())
c = [[0]*n for _ in range(m)]
wc = [[0]*n for _ in range(m)] # 물과 백조를 분리한다

a, swan = [], []

# 백조, 물을 각각 저장할 큐와 다음 위치를 저장할 임시 큐 해서 4개를 만든다
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

# 최초
for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if a[i][j] == 'L':
            swan.extend([i, j]) # 백조 저장
            wq.append([i, j]) 
        elif a[i][j] == '.':
            wc[i][j] = 1
            wq.append([i, j]) #물 저장

x1, y1, x2, y2 = swan
q.append([x1, y1]) # 최초로 순회
# 시작점이 백조 1이었기 때문에 백조 1에서부터 시작해 계속 돌아간 후
# 계속 얼음을 녹이면서 진행했을때 결국 거기 갈 수 있기만 하면 둘은 만날수가 있게 되는 것

a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0 # 횟수

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1

'''
내 풀이
유니언 파인드를 명시적으로 사용했는데, 그거때문에 메모리 초과가 난 것 같다
로직을 좀 더 다이어트 하는 연습이 필요하다..!

from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

R, C = map(int, input().split())
lake = [ list(input()) for i in range(R) ] 

groups = -1
beneath = []
swan = []

# visited = [[0 for c in range(C)] for i in range(R)]

for r in range(R):
  for c in range(C):
    if lake[r][c] == '.':
      groups += 1
      swan_flag = False
      beneath.append([])
      queue = deque([(r,c)])
      while queue:
        ar, ac = queue.popleft()
        for i in range(4):
          nr = ar + dr[i]
          nc = ac + dc[i]
          if (-1 < nr < R) and (-1 < nc < C):
            if lake[nr][nc] == '.':
              lake[nr][nc] = groups
              queue.append((nr, nc))
            elif lake[nr][nc] == 'X':
              beneath[groups].append((nr, nc))
            elif lake[nr][nc] == 'L':
              if not swan_flag:
                swan.append(groups)
                swan_flag = True

union_find = [i for i in range(groups+1)]

def find(x):
  while union_find[x] != x:
    x = find(union_find[x])
  return x

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    union_find[y] = x

def pathSearch(x, y):
  while union_find[x] != x:
    x = union_find[x]
    if x == y:
      return True
  return False

day = 1

while True:
  for i in range(len(union_find)):
    for r, c in beneath[i]:
      lake[r][c] = '.'

  new_beneath = [[] for _ in range(len(union_find))]

  for i in range(len(union_find)):
    for r, c in beneath[i]:
      if lake[r][c] == '.':
        queue = deque([(r,c)])
        while queue:
          ar, ac = queue.popleft()
          lake[ar][ac] = i
          for m in range(4):
            nr = ar + dr[m]
            nc = ac + dc[m]
            if (-1 < nr < R) and (-1 < nc < C):
              if (lake[nr][nc] == '.'):
                queue.append((nr, nc))
              elif lake[nr][nc] == 'X':
                new_beneath[i].append((nr, nc))
              elif (lake[nr][nc] != 'L') and (lake[nr][nc] > -1) and (lake[nr][nc] != i):
                union(lake[nr][nc], i)

  if pathSearch(swan[0], swan[1]) or pathSearch(swan[1], swan[0]):
    print(day)
    break
  
  day += 1
  beneath = new_beneath[:]
'''