import sys
import heapq

inf = sys.maxsize # inf보다 이게 더 시간이 좀 덜드는거 같다

V, E = map(int, input().split())
K = int(input())

# 모든 간선의 존재유무를 표현하지 않고 간선이 존재하는 노드만 표현
# 표현을 간결하게 하자
graph = [[] for _ in range(V)]

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u-1].append((w, v-1))

dist = [inf]*V
dist[K-1] = 0

queue = []
heapq.heappush(queue, (dist[K-1], K-1))

while queue:
  cur_dist, cur_node = heapq.heappop(queue)

  if dist[cur_node] < cur_dist:
    continue

  for w, nv in graph[cur_node]: # 뽑기 좋게 만들기
    distance = cur_dist + w

    if distance < dist[nv]:
      dist[nv] = distance
      heapq.heappush(queue, (distance, nv))

for d in dist:
  if d == inf:
    print('INF')
  else:
    print(d)

