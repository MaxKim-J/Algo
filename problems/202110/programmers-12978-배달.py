from math import inf
import heapq

'''
전형적인 다익스트라 문제
'''

def solution(N, road, K):
    answer = 0
    graph = [[inf]*N for _ in range(N)]
    
    for i in range(N):
        graph[i][i] = 0
        
    for r in road:
        a, b, d = r
        # 각 노드를 잇는 간선이 두개 이상 있을 수 있다는 조건이 있었다
        # 최소 경로를 구하는게 목적이므로 가중치가 더 작은 얘만 골라서 그래프에 넣어야 한다
        graph[a-1][b-1] = min(d, graph[a-1][b-1])
        graph[b-1][a-1] = min(d, graph[a-1][b-1])
        
    dist = [0] + [inf] * (N-1)
    queue = [(0,0)]
    
    while queue:
        node, distance = heapq.heappop(queue)
        
        # 현재 방문하는 노드까지의 최단거리가 (이미 기록되어서)
        # 현재 방문하는 노드까지 오는데 걸리는 거리보다 작다면 그 다음거는 갱신할 필요가 없다
        # 이미 최단경로로 node에서 뻗어나가는 경로는 계산이 되었기 때문이다
        # 이 조건은 노드를 백트랙킹하기위해 존재하는 셈이라고 할 수 있겠다
        if dist[node] < distance:
            continue
            
        for i in range(N):
            if graph[node][i] != inf and graph[node][i] != 0:
                new_distance = distance + graph[node][i]
                if dist[i] > new_distance:
                    dist[i] = new_distance
                    heapq.heappush(queue, (i, new_distance))
        
    
    return len(list(filter(lambda x:x<=K, dist)))