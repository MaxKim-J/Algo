import heapq

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
  # graph의 key를 문자열로
   distances = {node: float('inf') for node in graph}
   distances[start] = 0 # 시작점의 거리는 0
   # 힙에는 이렇게 들어감 [거리, 시작점]
   heapq.heappush(queue, [distances[start], start])

   while queue:
     # 현재 방문한 노드들중 가장 거리가 작은것부터 먼저 순회
     current_distance, current_node = heapq.heappop(queue)

    # 현재 기록된 시작점으로부터 해당 노드까지의 최소경로가
    # 현재 노드까지 진입했을때의 최단 거리보다 작으면
    # 더 볼게 없음 더해봤자 작은거임
     if distances[current_node] < current_distance:
       continue

    # 현재 순회 노드에 붙어있는 노드, 간선들을 순회
     for adjacent, weight in graph[current_node].items():

      # 현재까지의 거리에 붙어있는 간선 중 하나의 거리를 더함
       distance = current_distance + weight

      # 현재 기록된 거리보다 간선의 거리를 하나 더한게 더 작으면
      # 이때만 큐에 넣음
       if distance < distances[adjacent]:
        # 새롭게 기록하고
        distances[adjacent] = distance
        # 노드까지의 새로운 거리를 우선순위큐에 집어넣는다
        heapq.heappush(queue, [distance, adjacent])

    # 큐에 남은게 없으면 거리 리턴
    return distances

    

