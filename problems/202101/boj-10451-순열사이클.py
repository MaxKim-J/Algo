from collections import deque

# 이분 그래프랑 거의 똑같다
# 한번에 모두 순회할 수 없는 그래프가 있다는 것을 명시하자


def BFS(start, graph):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    graph = {i+1: [] for i in range(N)}
    for i in range(1, N+1):
        graph[P[i-1]].append(i)
        graph[i].append(P[i-1])
    count = 0
    visited = {i+1: False for i in range(N)}
    for j in P:
        if visited[j] == False:
            count += 1
            BFS(j, graph)

    print(count)
