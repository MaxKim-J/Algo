graph = {
  'A': {'B':2, 'C':4},
  'B': {'D':3, 'E':2},
  'C': {},
  'D': {'F':2},
  'E': {'F': 4},
  'F': {}
}

def bellman_ford(graph, start):
  # 거리를 저장하는 맵
  dist = dict()

  # 초기화
  for node in graph:
    dist[node] = float('inf')

  dist[start] = 0

  # v-1번의 라운드
  for i in range(len(graph) - 1):
    for node in graph: # 노드를 전부 순회(다익스트라와는 다르게 순서대로 순회)
      for neighbor in graph[node]: # 노드에 접한 정점들 모두 순회
        # 현재 dist에 기록된 거리보다 dist에다가 graph의 간선의 가중치를 더한게 더 작으면
        # 갱신한다
        if dist[neighbor] > dist[node] + graph[node][neighbor]:
          dist[neighbor] = dist[node] + graph[node][neighbor]

    print(dist)

  # 음의 사이클 유무를 확인할 수 있는 로직
  for node in graph:
    for neighbor in graph[node]:
      # 노드에 속한 정점들을 모두 순회했을때
      # 정점을 이동했을때 오히려 더 거리가 줄어들면 음수 사이클이 존재하는 것
      if dist[neighbor] > dist[node] + graph[node][neighbor]:
        return -1

  return dist

print(bellman_ford(graph, 'A'))