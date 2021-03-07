'''
위상 정렬 : 순서가 정해져 있는 작업을 차례로 수행해야 할 때, 데이터의 순서를 결정하는 알고리즘

1. 진입차수가 0인 정점을 찾아 큐(힙)에 삽입함
2. 원소를 꺼내 원소와 붙은 간선을 제거
3. 제거 이후에 진입차수가 0이 된 정점을 또 큐에 삽입
4. 큐가 빌때까지 반복
5. 이때 그래프간 사이클이 존재하면 안됨(시작점을 찾을 수가 없음)
6. 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상정렬의 결과
'''

# 파이썬에서는 민힙 : 항상 가장 작은 값이 나온다
import heapq

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

# 진입차수 기록하기
indegree = [0] * (n+1)

heap = []
result = []

# 간선 정보를 입력으로 받아 그래프 구성
for _ in range(m):
    x, y = map(int, input().split())
    # 연결된거 기록
    graph[x].append(y)
    # 진입차수 값 계산
    indegree[y] += 1

# 진입차수 0인 정점들을 다 큐에 넣음
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

# 왜 힙에 넣는가? : 그냥 큐를 사용해도 무방하지만, 각 일에 번호가 매겨져있는 경우
# 가능하다면 가장 작은 번호가 선행되서 없어지게 하려면 우선순위 큐를 사용한다
# 한번 삽입 삭제시에 log n시간이 소요되기 때문에 n^2이 걸리는 min을 사용하는 것보다 시간이 줄어든다
while heap:
    data = heapq.heappop(heap)
    # 큐에서 꺼냈을 때 result 배열에 넣는다
    result.append(data)
    # 힙에서 꺼낸 정점과 연결되어있는 정점의 차수를 하나씩 줄인다
    for y in graph[data]:
        indegree[y] -= 1
        # 차수를 줄였을 때 진입차수가 0이 되었다면 그 정점을 큐에다가 넣는다
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for i in result:
    print(i, end=' ')