from collections import defaultdict
from heapq import *

# 이번엔 간선만 있음
myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

def prim(start_node, edges):
    mst = []
    adjacent_edges = defaultdict(list)

    # 간선들 순회하면서 모든 간선 정보 저장하기
    # key는 정점임
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    # 임의의 정점 선택해서 연결된 노드 집합에 삽입하기
    # 크루스칼과 다르게 하나의 집합으로만 계속 유지하고, 하나씩 더함
    connected_nodes = set(start_node)

    # 최초 정점의 간선 리스트
    candidate_edge_list = adjacent_edges[start_node]

    # 간선 리스트를 히피파이해서(sort) 최소값을 쉽게 pop할수 있게 만듬
    heapify(candidate_edge_list)
    
    # 간선 리스트 계속 유지
    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list) # 최소인거 하나 뽑음
        # 집합에 연결되어 있지 않은 친구라면
        if n2 not in connected_nodes:
            connected_nodes.add(n2) # 집합에 넣고
            mst.append((weight, n1, n2)) # 신장트리에 넣음 
            
            # 그리고 연결된 정점으로 가서 거기는 집합에 들어있지 않은지 확인하기
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes: # 간선에 접합이 된 다른쪽이 집합에 있는지 확인하는거
                    # 집합에 들어있지 않은 얘들은 순회하기 위해 heappush => 이런식으로 모든 간선 순회
                    heappush(candidate_edge_list, edge)

    return mst