# 접근은 정말 잘 맞아들어갔지만 디테일이 딸려서 정답까진 도출을 못한 문제

# ? 스켈레톤 코드를 꼭 + 빨리 작성하고 이 드래프트를 완성시킨다는 생각으로 여러번 보는게 맞다
# ? 그리고 이를 코드로 옮기는 과정에서 실수가 없는지 반복해서 검증한다.

# 중량제한 리밋이 10억이므로 **찾고자 하는 이 중량**에 대해 이진탐색을 수행하면 log로 수행시간 떨어짐
# 공장에서 시작해서 다른 공장까지 닿는 모든 경우의 수는 BFS로 탐색한다
# 일단 중량 크기가 존나 크니까 log를 씌워야겠다고 생각이 팍 들어야함

#! 연산 개수를 정확히 캐치해내자...! log가 씌워지면 연산이 어느정도로 줄지도 생각해야한다.
#! 연산 개수를 캐치해내지 못하니까 문제 푸는 내내 불안한거다
# * 이 경우는 이진탐색때문에 연산이 Log십억 = 30정도로 떨어지고,
# * BFS는 간선의 개수만큼 반복을 수행하고, 이것으로 시간 복잡도를 판단할 수 있는데
# * 섬을 잇는 다리, 즉 그래프의 간선의 개수가 10000개 정도이므로 10000 * 30 = 3000000개 연산 => 1초만에 풀기 쌉가능

from collections import deque

island, bridge = map(int, input().split())
bridges = {i+1: [] for i in range(island)}


def BFS(origin, target, weight):
    queue = deque([origin])
    visited = [False] * (island + 1)
    visited[origin] = True
    while queue:
        visit = queue.popleft()
        # 여기서 객기부리지 말자 경로에 있는건 다 돌아야된다 왜 그걸 모르노
        for y, l in bridges[visit]:
            if not visited[y] and l >= weight:
                visited[y] = True
                queue.append(y)
    return visited[target]


#! 이진탐색의 데이터를 뽑을때 꼭 배열로 정렬해서 할 필요는 없다
# 걍 최대최소부터 시작해서 범위를 줄일수 있으면 되는거고
start = 1000000000
end = 1

for _ in range(bridge):
    X, Y, L = map(int, input().split())
    bridges[X].append((Y, L))
    bridges[Y].append((X, L))
    start = min(start, L)
    end = max(end, L)

origin, target = map(int, input().split())

# 시작할때는 최소 중량으로 무게를 초기화함 => 그래야 길을 못찾았을때 이 값이 반환되니까
result = start

#! 이거 걍 외우자
# 같을때부터 일단 벗어나야하니까 <=
while start <= end:
    # ? 이진탐색으로 구해야하는 값이 무엇인지에 대해 생각해야한다.
    mid = (start+end) // 2
    if BFS(origin, target, mid):
        #! result를 기억해야 하는 시점은 start를 마지막으로 올려서 start와 end를 같은값으로 만드는 그 시점이다
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
