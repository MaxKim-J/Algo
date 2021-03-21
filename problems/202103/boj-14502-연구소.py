'''
메모리가 매우 넉넉...
식이 다 말이 되었다고 생각이 들어도... 답이 안나온다면
여기까진 맞았다는 확신이 드는 곳 근처에서 print를 갈겨보면 버그 찾을 가능성이 높아짐
중간 검산을 잘 못해서 시간을 많이 뺐겼다

DFS+BFS
'''

from collections import deque
import sys

sys.setrecursionlimit(100000)

N, M = map(int, input().split())

board = []
for _ in range(N):
  board.append(list(map(int, input().split())))

virus = []
whole_zero = 0

for i in range(N):
  for j in range(M):
    if board[i][j] == 2:
      virus.append((i,j))
    elif board[i][j] == 0:
      whole_zero += 1

def evaluate(walls):
  dr = [0,0,1,-1]
  dc = [1,-1,0,0]

  count = 0
  visited = [[0] * M for _ in range(N)]
  for pos in virus:
    queue = deque([pos])
    while queue:
      r, c = queue.popleft()
      for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (-1 < nr < N) and (-1 < nc < M) and (visited[nr][nc] == 0):
          if (board[nr][nc] == 0) and ((nr, nc) not in walls):
            count += 1
            visited[nr][nc] = 1
            queue.append((nr, nc))
  return whole_zero - (count + 3)


def DFS(depth, walls):
  global result
  if depth == 3:
    result = max(result, evaluate(walls))
    return
  for r in range(N):
    for c in range(M):
      if (board[r][c] == 0) and ((r,c) not in walls):
        new_walls = walls[:]
        new_walls.append((r,c))
        DFS(depth + 1, new_walls)


result = 0

DFS(0, [])

print(result)

# N = 8
# M = 8
# board = [
#   [2, 0, 0, 0, 0, 0, 0, 2],
#   [2, 0, 0, 0, 0, 0, 0, 2],
#   [2, 0, 0, 0, 0, 0, 0, 2],
#   [2, 0, 0, 0, 0, 0, 0, 2],
#   [2, 0, 0, 0, 0, 0, 0, 2],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
# ]

# N = 4
# M = 6
# board = [
#   [0, 0, 0, 0, 0, 0],
#   [1, 0, 0, 0, 0, 2],
#   [1, 1, 1, 0, 0, 2],
#   [0, 0, 0, 0, 0, 2],
# ]

# N = 7
# M = 7
# board = [
#   [2,0,0,0,1,1,0],
#   [0,0,1,0,1,2,0],
#   [0,1,1,0,1,0,0],
#   [0,1,0,0,1,1,0],
#   [0,0,0,0,0,1,1],
#   [0,1,0,0,0,0,0],
#   [0,1,0,0,0,0,0],
# ]