
#? 내풀이 - 시간초과
'''
최소 이동 횟수를 구하는 문제인데 완전탐색, 혹은 완성되는 경로를 반복하는 DFS로는 가망이 없어서
BFS로 각 더러운 포인트까지 나눠서 경로를 완성하는 접근은 맞았음
그런데 내가 푼 방식이 정말 최소의 이동거리만 소비하는 경로냐 라는 것을 간과함
출발지점에서 최대한 가까운 더러운 곳 포인트들만 이동하면 최소라고 생각했는데

6 5
.....*
.*..*.
...o..
.*....
......

이런 테케는 성립하지 않음(백준 테케 너무 적다 이거야....)
결국 BFS를 별 개수만큼이 아니라 모든 순열을 조합하여 여러번 해야한다고 생각했는데(트리를 이루는 BFS) 그것도 시간초과되서

BFS 여러번을 모든 o와 *, * 과 * 사이의 거리를 모두 구한 후에 순열을 순회하면서
거리를 모두 더해보고 가장 최소값을 찾는 방법으로 풀어야 시간 안에 풀 수 있었다
순열은 생각했었는데 순열 마다 BFS를 땡기면 그거는 그것대로 또 안된다 시간초과(...)

중요한건 그게 정말 최소냐! 그렇게 픽하는게 진짜 최소를 보장하냐! 의심해볼것.
그리디한 상황은 많지 않다. 경험적으로 알고 있지만...
어쨋든 그런 상황 간과하지 말자
뭔가 모두 해보고 나중에 그 값을 토대로 정답에 가까운 값을 계산하는 유형이 가장 빠른 경우가 있는 듯 하다
플로이드 와샬같은 경우도 그렇고...
'''
from collections import deque
from copy import deepcopy
from itertools import permutations

dr = (0,0,1,-1)
dc = (1,-1,0,0)

def BFS(path, board, current_cost, w, h):
  global new_start_points, new_costs
  queue = deque([(path[-1], 0)])
  visited = [[0]*w for _ in range(h)]
  visited[path[-1][0]][path[-1][1]] = -1
  while queue:
    pos, depth = queue.popleft()
    r, c = pos
    if board[r][c] == '*':
      new_start_points.append(path + [(r,c)])
      new_costs.append(current_cost + depth)
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if -1 < nr < h and -1 < nc < w:
        if board[nr][nc] != 'x' and visited[nr][nc] == 0:
          queue.append(((nr,nc), depth+1))
          visited[nr][nc] = -1

while True:
  w, h = map(int, input().split())
  
  if w == 0 and h == 0:
    break

  board = []
  dirty = 0
  start_points = []
  costs = [0]

  for i in range(h):
    row = list(input())
    for j in range(w):
      if row[j] == '*':
        dirty += 1
      if row[j] == 'o':
        start_points.append([(i, j)])
    board.append(row)

  for d in range(dirty):
    new_start_points = []
    new_costs = []
    for i in range(len(costs)):
      new_board = deepcopy(board)
      for sr, sc in start_points[i]:
        new_board[sr][sc] = '.'
      BFS(start_points[i], new_board, costs[i], w, h)
    if d == 0 and len(new_costs) != dirty:
      costs = -1
      break
    costs = new_costs
    start_points = new_start_points
  
  print(min(costs) if costs != -1 else -1)


#* 남의 풀이 

from collections import deque
from itertools import permutations
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    c = [[0]*w for _ in range(h)]
    q.append([x, y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if a[nx][ny] != 'x' and not c[nx][ny]:
                    c[nx][ny] = c[x][y] + 1
                    q.append([nx, ny])
    return c


while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    a, d = [], []
    for i in range(h):
        row = list(input().strip())
        a.append(row)
        for j, k in enumerate(row):
            if k == 'o':
                sx, sy = i, j
            elif k == '*':
                d.append([i, j])

    # 시작점으로부터 모든 *에 관한 거리 구하기,
    r2d, flag = [], 0
    c = bfs(sx, sy)
    for i, j in d:
        if not c[i][j]:
            flag = 1
            break
        r2d.append(c[i][j]-1)
    if flag:
        print(-1)
        continue

    # 모든 *과 *에 관한 거리를 구해놓고
    d2d = [[0]*len(d) for _ in range(len(d))]
    for i in range(len(d)-1):
        c = bfs(d[i][0], d[i][1])
        for j in range(i+1, len(d)):
            d2d[i][j] = c[d[j][0]][d[j][1]]-1
            d2d[j][i] = d2d[i][j]

    # 순열로 갈 수 있는 모든 경로를 다 더해본 후
    p = list(permutations([i for i in range(len(d2d))]))

    ans = sys.maxsize

    # 순열의 경로를 순회하며 모든 거리를 다 더해본다
    for i in p:
        dist = 0
        dist += r2d[i[0]]
        nfrom = i[0]
        for j in range(1, len(i)):
            nto = i[j]
            dist += d2d[nfrom][nto]
            nfrom = nto
        ans = min(ans, dist)
    print(ans)