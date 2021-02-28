'''
짚어보는 트리의 정의

1. 그래프의 일종 => 트리도 그래프
2. 각 노드를 연결하는 선은 단 하나 => 여러 노드가 한 노드를 가리킬 수 없음
3. 사이클이 없음 => 루트와 리프가 존재함
4. 각 노드가 0개 이상의 자식노드를 가지고 있다 => 절대 끊어져있지 않음
'''

#! 핵심 아이디어 : 노드 x에서 가장 먼 노드를 y라고 했을 때, y는 지름을 이루는 노드 중 하나 => DFS두번
# 임의의 노드 x에 대해 DFS(x)에서 최장거리를 이루는 y를 구하고, DFS(y)를 구해 최장길이를 더하면 노드의 지름 구할 수 있음

V = int(input())
matrix = [[] for _ in range(V+1)]

for _ in range(V):
    path = list(map(int, input().split()))
    path_len = len(path)
    for i in range(1, path_len//2):
        # 간선을 종착점과 거리를 튜플로 해당 노드의 인덱스에다가 저장
        matrix[path[0]].append((path[2*i-1], path[2*i]))


def DFS(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0:
            # 정점당 거리 업뎃
            result[e] = result[start] + d
            DFS(e, matrix, result)


result1 = [0 for _ in range(V+1)]
DFS(1, matrix, result1)    # 여기는 어디가 시작점이든 상관이 없다
result1[1] = 0  # 다만 루트로 삼았던 거리는 0처리해준다 => 양방향으로 간선이 들어있기 때문에 루트도 같이 업뎃되기 때문

tmpmax = 0
index = 0

# 시작노드로부터 가장 긴 거리를 가지고 있는 인덱스값 구하기
for i in range(len(result1)):
    if tmpmax < result1[i]:
        tmpmax = result1[i]
        index = i

# 그 인덱스값으로부터 다시 DFS 시작해서 가장 긴거리를 구함
result2 = [0 for _ in range(V+1)]
DFS(index, matrix, result2)
result2[index] = 0  # 여기도 마찬가지로 루트 0처리

print(max(result2))
