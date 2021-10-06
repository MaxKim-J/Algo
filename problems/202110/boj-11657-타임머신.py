from math import inf
import sys

input = sys.stdin.readline

def bellman_ford(n, m, graph):
  dist = [0] + [inf]*(n-1)
  
  for r in range(n):
    for j in range(m): # 벨만 포드는 노드의 개수만큼 간선을 계속해서 relax해주는 알고리즘이기 때문에
      # 간선 정보만 확보만 되면 되서 굳이 완성된 이차원 배열로 그래프를 표현할 필요가 없다
      if dist[graph[j][1]] > dist[edges[j][0]] + edges[j][2]:
        dist[graph[j][1]] = dist[edges[j][0]] + edges[j][2]
        if r == n-1: # 마지막으로 갈때 갱신이 되면 음의 사이클이 존재하는 것이다
          return False

  return dist
    
N, M = map(int, input().split())
edges = []

for _ in range(M):
  u, v, w = map(int, input().split())
  edges.append((u-1, v-1, w))

result = bellman_ford(N, M, edges)

if result == False:
  print(-1)
else:
  for i in range(1, N):
    print(-1 if result[i] == inf else result[i])