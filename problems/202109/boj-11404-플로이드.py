from math import inf
from copy import deepcopy

n=int(input())
m=int(input())

graph=[[inf]*n for _ in range(n)]

for _ in range(m):
  i, j, w = map(int, input().split())
  graph[i-1][j-1] = min(graph[i-1][j-1], w)

for k in range(n):
  graph[k][k] = 0

dist = deepcopy(graph)

for k in range(n):
  for i in range(n):
    for j in range(n):
      if dist[i][j] > dist[i][k] + dist[k][j]:
        dist[i][j] = dist[i][k] + dist[k][j]

for r in range(n):
  for c in range(n):
    if dist[r][c] == inf: # 0으로 덮어 씌워야 했음
      print(0, end=' ')
      continue
    print(dist[r][c], end=' ')
  print()