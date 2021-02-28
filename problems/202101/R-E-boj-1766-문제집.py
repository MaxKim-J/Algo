# 위상정렬 : 순서가 정해져 있는 작업을 차례로 수행해야 할때, 데이터의 순서를 결정해줌
# O(v+e)

# 진입차수가 0인 정점을 큐(힙)에 삽입 => 원소를 꺼내 원소와 간선을 제거 => 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입
# 큐가 빌때까지 반복
# 사이클이 존재하면 안됨(시작점을 찾을 수가 없어서) => 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상정렬의 결과

#! 뭐가 쉽다 정보가 주어졌을 때 이것을 이어져있는 노드라고 생각할 수 있는골까?
# 무조건 뒤에 온다는 정보니까 일단 앞에 뭐가 없는(진입간선이 없는) 얘들부터 풀고
# 문제를 풀었을 때 이어져있는 간선은 없애는 것 => 이미 먼저 풀었으니 다른 얘들은 이제 풀어도 별 문제 없음

import heapq

n, m = map(int, input().split())
array = [[] for i in range(n+1)]
indegree = [0] * (n+1)

heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    # 연결된거 기록
    array[x].append(y)
    # 진입차수 값 계산
    indegree[y] += 1

# 0인 얘들 다 일단 큐에 넣음
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    # 거기서 이동할 수 있는 곳으로 다 가서 간선 제거
    # 그리고 다시 진입차수가 0인 얘들 푸쉬
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for i in result:
    print(i, end=' ')
