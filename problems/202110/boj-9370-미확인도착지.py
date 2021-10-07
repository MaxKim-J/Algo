'''
엣지 케이스를 초반에 잘 찾지 못했어서 좀 해맸다

엣지 케이스 : 최단 거리가 같은데 정해진 경로를 pass한 경우와 안 한 경우가 존재할 수 있는데
경로가 발견된 순서에 따라서 pass한 경우보다 pass하지 않은 경우가 reachable에 기록될 가능성이 있었음

이제 엣지 케이스나 반례를 스스로 찾을 수 있는 단계로 가야한다. 
BFS 비슷한것들은(다익스트라도 그렇고) 정말 최적값이 내가 기록하고자 하는 곳에 정확히 기록되는지 잘 생각해보자
그리고 다익스트라 코드는 이제 외운 것 같다. 개념 좀만 보충하면 더 잘 이해할 수 있을듯
'''


from math import inf
import heapq

def dijkstra(n, start, point1, point2, graph):
  dist = [inf] * (n+1)
  dist[start] = 0

  is_reachable = [False] * (n+1)
  queue = []
  heapq.heappush(queue, (dist[start], start, False))

  while queue:
    current_dist, node, is_pass = heapq.heappop(queue)

    if dist[node] < current_dist: # 요기 부분만 헷갈리지 말자
      continue

    for i in range(1, n+1):
      neighbor_dist = graph[node][i]
      if (neighbor_dist != inf) and (neighbor_dist != 0):
        new_distance = current_dist + neighbor_dist
        new_is_pass = is_pass

        if (node == point1 and i == point2) or (node == point2 and i == point1):
          new_is_pass = True

        if dist[i] > new_distance:
          dist[i] = new_distance
          is_reachable[i] = new_is_pass
          heapq.heappush(queue, (new_distance, i, new_is_pass))
        elif dist[i] == new_distance: 
          if is_reachable[i] == False and new_is_pass == True:
            is_reachable[i] = new_is_pass
            heapq.heappush(queue, (new_distance, i, new_is_pass))

  return is_reachable

T = int(input())

for _ in range(T):
  n,m,t = map(int, input().split())
  s,g,h = map(int, input().split())
  graph = [[inf]*(n+1) for _ in range(n+1)]

  for _ in range(m):
    a,b,d = map(int, input().split())
    graph[a][b] = d
    graph[b][a] = d

  for i in range(1, n+1):
    graph[i][i] = 0

  candidate = []
  for _ in range(t):
    node = int(input())
    candidate.append(node)

  reachable = dijkstra(n, s, g, h, graph)

  result = sorted(list(filter(lambda x:reachable[x] == True, candidate)))
  result = list(map(lambda x:str(x), result))
  print(' '.join(result))