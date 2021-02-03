from collections import deque
'''
그래프에 기록된 바가 양방향이어야 하는지, 단방향이어야 하는지 생각해야한다
트리의 지름 문제는 대표적으로 양방향으로 기록되어야 하는데

단방향으로 순서대로 기록해버리면 나중에 두번째 순회를 시작할 지점을 찾았을때
아무런 노드로도 갈 수 없는 상황이 벌어지기 때문이다..
이번 문제 입력은 정렬되서 들어온다는 조건이 있었는데, 그렇다고 해도 양방향 기록이 필요함

순회는 DFS가 더 좋나..? => 끝까지 빨리 가야 좋다 => 어짜피 dist 배열에는 말단값
근데 또 별차이 없을거 같기도

간선을 두번 순회하기때문에 O(2n-2) ==> O(n)
'''

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, n, e = map(int, input().split())
    graph[i].append((n, e))
    graph[n].append((i, e))


def DFS(start, shot):
    dist = [0 for _ in range(N+1)]
    stack = deque([start])
    while stack:
        current = stack.pop()
        for (node, edge) in graph[current]:
            if dist[node] == 0:
                dist[node] = dist[current] + edge
                stack.append(node)
    if shot == 'first':
        max_value = 0
        new_start = 0
        # 시작점의 거리를 해소한다 => 양방향이기 때문
        dist[1] = 0
        for i in range(2, N+1):
            if dist[i] > max_value:
                new_start = i
                max_value = dist[i]
        return new_start
    else:
        # 시작점의 거리를 해소한다 => 양방향이기 때문
        dist[start] = 0
        return max(dist)


second_start = DFS(1, 'first')
result = DFS(second_start, 'second')
print(result)
