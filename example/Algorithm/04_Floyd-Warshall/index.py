from math import inf

def floyd_warshall(n, graph):
  dist = [[inf]*n for i in range(n)] # n은 정점의 수, 최단 경로 담는 배열

  for i in range(n):
    for j in range(n):
      dist[i][j] = graph[i][j]
  
  # 가장 바깥 포문이 "거치는 정점"이라서 거치는 정점을 기준으로 순회한다는 느낌이 됨
  # 시작점, 끝점, 중간점을 모두 각각 순회하기 때문에 3중포문이 필요한거였음
  for k in range(n): # 거치는 점
    for i in range(n): # 시작점
      for j in range(n): # 끝점
        if dist[i][j] > dist[i][k] + dist[k][j]:
          # 현재 기록된 최소 경로보다 특정 점을 거쳐서 가는 것이 짧으면 그걸루 갱신
          dist[i][j] = dist[i][k] + dist[k][j]

  return dist

n = 4
graph = [
  [0,2,inf,4],
  [2,0,inf,5],
  [3,inf,0,inf],
  [inf,2,1,0],
]

dist = floyd_warshall(n, graph)

for i in range(n):
  for j in range(n):
    print(dist[i][j], end='')
  print()