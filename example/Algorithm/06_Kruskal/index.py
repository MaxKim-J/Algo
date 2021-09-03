# 뭐 만약에 이걸 쓸일이 있다 치면 뭐 대충 간선을 정렬하기 좋은 형태로
# 가공을 해야할 것이다
mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

def find(node):
  if parent[node] != node: # 집합의 대장이 아닐 경우 계속 따라가서 찾는다
    parent[node] = find(parent[node])
  return parent[node]

def union(node_v, node_u):
  root1 = find(node_v) # find를 통해 두 집합의 대장을 찾아낸다
  root2 = find(node_u)

  # 트리의 height 정보를 바탕으로 큰쪽에 작은쪽을 연결한다
  if rank[root1] > rank[root2]:
    parent[root2] = root1 # 순순히 붙는 경우 rank의 변화는 따로 없음
  else:
    parent[root1] = root2
    # 높이가 같다면 한쪽에 높이를 상승시키고 다른쪽 트리를 붙인다
    if rank[root1] == rank[root2]:
      rank[root2] += 1

def make_set(node):
  parent[node] = node
  rank[node] = 0

def kruskal(graph):
  mst = []
  
  # 초기화, 단일 집합 만들기
  for node in graph['vertices']:
    make_set(node)

  edges = graph['edges']
  edges.sort()

  for edge in edges:
    weight, node_v, node_u = edge
    if find(node_v) != find(node_u):
      union(node_v, node_u)
      mst.append(edge) # 신장 트리는 그래서 엣지들의 집합으로 나옴

  return mst
