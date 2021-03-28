# n = 6
# m = 6
# office = [
#   ['0', '0', '0', '0', '0', '0'],
#   ['0', '2', '0', '0', '0', '0'],
#   ['0', '0', '0', '0', '6', '0'],
#   ['0', '6', '0', '0', '2', '0'],
#   ['0', '0', '0', '0', '0', '0'],
#   ['0', '0', '0', '0', '0', '5'],
# ]

# n = 6
# m = 6
# office = [
#   ['1', '0', '0', '0', '0', '0'],
#   ['0', '1', '0', '0', '0', '0'],
#   ['0', '0', '1', '0', '0', '0'],
#   ['0', '0', '0', '1', '0', '0'],
#   ['0', '0', '0', '0', '1', '0'],
#   ['0', '0', '0', '0', '0', '1'],
# ]

# n = 4
# m = 6
# office = [
#   ['0', '0', '0', '0', '0', '0'],
#   ['0', '0', '0', '0', '0', '0'],
#   ['0', '0', '1', '0', '6', '0'],
#   ['0', '0', '0', '0', '0', '0'],
# ]

# n = 1
# m = 7
# office = [
#   ['0', '1', '2', '3', '4', '5', '6'],
# ]


import copy

n, m = map(int, input().split())
office = []

for _ in range(n):
  office.append(input().split())

cctv = []
for i in range(n):
  for j in range(m):
    if office[i][j] != '0' and office[i][j] != '6':
      cctv.append((i, j))

def get_directions(type):
  if type == '1':
    return [[(0,1)], [(0,-1)], [(1,0)], [(-1,0)]]
  elif type == '2':
    return [[(0,1), (0,-1)], [(1,0),(-1,0)]]
  elif type == '3':
    return [[(-1,0), (0,1)], [(0,1), (1,0)], [(1,0), (0,-1)], [(0,-1), (-1,0)]]
  elif type == '4':
    return [[(0,-1), (-1,0), (0,1)], [(-1,0),(0,1),(1,0)], [(0,1),(1,0),(0,-1)], [(0,-1),(-1,0),(0,1)]]
  elif type == '5':
    return [[(0, 1), (0, -1), (1, 0), (-1, 0)]]

result = m * n

def DFS(office, depth):
  global result

  if depth == len(cctv):
    blind_spot = 0
    for i in range(n):
      for j in range(m):
        if office[i][j] == '0':
          blind_spot += 1
    result = min(result, blind_spot)
    return
  
  r, c = cctv[depth]
  for direction in get_directions(office[r][c]):
    new_office = copy.deepcopy(office)
    for sr, sc in direction:
      nr = r + sr
      nc = c + sc

      if sr == 0:
        # 우 (0, 1)
        if sc == 1:
          for i in range(nc, m):
            if new_office[nr][i] == '6':
              break
            if new_office[nr][i] == '0':
              new_office[nr][i] = '#'
        # 좌 (0, -1)
        else:
          for i in range(nc, -1, -1):
            if new_office[nr][i] == '6':
              break
            if new_office[nr][i] == '0':
              new_office[nr][i] = '#'
      elif sc == 0:
        # 상 (-1, 0)
        if sr == -1:
          for i in range(nr, -1, -1):
            if new_office[i][nc] == '6':
              break
            if new_office[i][nc] == '0':
              new_office[i][nc] = '#'
        # 하 (1, 0)
        else:
          for i in range(nr, n):
            if new_office[i][nc] == '6':
              break
            if new_office[i][nc] == '0':
              new_office[i][nc] = '#'

    DFS(new_office, depth + 1)


DFS(office, 0)
print(result)


'''
from copy import deepcopy
import sys
input = sys.stdin.readline

def fill(x, y, arr, d):
    for i in d:
        nx, ny = x, y
        # 전진하는 느김으로 처리하면 쉬웠다..
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 6:
                    break
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = "#"
            else:
                break

def dfs(arr, cnt):
    global result
    temp = deepcopy(arr)
    if cnt == cctv_cnt:
        num = 0
        for i in range(n):
            num += temp[i].count(0)
        result = min(result, num)
        return
    x, y, cctv = q[cnt]
    for i in direction[cctv]:
        fill(x, y, temp, i)
        dfs(temp, cnt + 1)
        temp = deepcopy(arr) # 아...이렇게하면 되겠구나..

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]], 
[[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

n, m = map(int, input().split())
s = []
q = []

cctv_cnt = 0
result = 100000000

for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(len(a)):
        if a[j] != 0 and a[j] != 6:
            q.append([i, j, a[j]])
            cctv_cnt += 1
dfs(s, 0)
print(result)
'''