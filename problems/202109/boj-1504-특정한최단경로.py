import sys
import heapq

inf = sys.maxsize

N, E = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(E):
  a,b,c = map(int, input().split())
  graph[a-1].append((b-1, c))
  graph[b-1].append((a-1, c))

v1, v2 = map(int, input().split())
v1 -= 1
v2 -= 1

def dijkstra(start, end):
  dist = [inf] * N
  dist[start] = 0

  queue = []
  heapq.heappush(queue, (dist[start], start))

  while queue:
    cur_dist, cur_node = heapq.heappop(queue)

    if dist[cur_node] < cur_dist:
      continue

    for nv, w in graph[cur_node]:
      new_dist = cur_dist + w
      if new_dist < dist[nv]:
        dist[nv] = new_dist
        heapq.heappush(queue, (new_dist, nv))

  return dist[end]

path1 = dijkstra(0, v1) + dijkstra(v1, v2) + dijkstra(v2, N-1)
path2 = dijkstra(0, v2) + dijkstra(v2, v1) + dijkstra(v1, N-1)

if path1 >= inf and path2 >= inf:
  print(-1)
else:
  print(min(path1, path2))
      