# 배추들이 모여있는 곳에 배추흰지렁이가 한마리만 있으면 되므로
# 서로 인접해있는 배추들이 몇 군대에 퍼져있는지 조사하면 총 몇마리 지렁이 필요한지 알 수 있음
# 즉 연결요소들이 개수를 구하는 문제 => DFS, BFS를 순회한 총 개수를 센다
# 일단 모든 칸을 순회하고 1을 만나면 DFS, BFS를 시작한다
# DFS로 풀면 setrecursionlimit()

import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
  #! 얘는 중간에 멈추는 조건이 딱히 필요하지 않음 그냥 돌게 없으면 끝내면 되서
  visited[x][y] = True
  directions = [(-1,0), (1,0), (0,-1), (0,1)]
  for dx, dy in directions:
    nx, ny = x + dx, y + dy
    # 범위를 넘어가는 경우
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    # 범위 안에서 아직 돌지 않은 경우
    if array[nx][ny] and not visited[nx][ny]:
      dfs(nx, ny)

for _ in range(int(input())):
  m, n, k = map(int, input().split())
  array = [[0] * m for _ in range(n)]
  visited = [[False] * m for _ in range(n)]
  for _ in range(k):
    y, x = map(int, input().split())
    array[x][y] = 1
  result = 0
  for i in range(n):
    for j in range(m):
      # 1일때 DFS 순회
      if array[i][j] and not visited[i][j]:
        dfs(i, j)
        result += 1
  print(result)