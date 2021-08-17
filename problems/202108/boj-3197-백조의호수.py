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
              if not swan_flag: # 백조 두마리가 같은 그룹에 있을수도 있음
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
