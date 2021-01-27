from collections import deque


def is_BG(start, graph):
    queue = deque([(start, 'A')])
    while queue:
        value, group = queue.popleft()
        for i in graph[value]:
            # B를 넣을 차례인데 A에 이미 있는거면 => 망함
            if group == 'A':
                if visited[i] == 'A':
                    return 'NO'
                elif visited[i] == 'B':
                    pass
                elif visited[i] == None:
                    visited[i] = 'B'
                    queue.append((i, 'B'))
            # A를 넣을 차례인데 B에 이미 있는거면 => 망함
            if group == 'B':
                if visited[i] == 'B':
                    return 'NO'
                elif visited[i] == 'A':
                    pass
                elif visited[i] == None:
                    visited[i] = 'A'
                    queue.append((i, 'A'))
    return 'YES'


k = int(input())

for _ in range(k):
    V, E = map(int, input().split())
    graph = {i+1: [] for i in range(V)}
    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    visited = {i+1: None for i in range(V)}
    ans = ''
    # * 이렇게 순회를 안해서 틀림
    for i in range(1, V+1):
        if visited[i] == None:
            ans = is_BG(i, graph)
            if ans == 'NO':
                break
    print(ans)

# BFS를 한번만 하는게 아니라 모든 노드를 시작점으로 해서 다 돌았어야 했음
#! BFS를 한다고 해서 모든 노드를 정말로 순회할 수 있는게 맞는가?????
#! 어떠한 시작점에서 BFS를 한다고 했을때, 연결이 안되있는? 이라고 해야대나 순회를 할 수 없는 노드가 있다면?
#! 그래프의 모든 노드에 대한 순회를 마치는 여부는 while이 끝날때가 아니고 visited로 판단하는게 옳다.
#! 연결점이 끊긴 그래프는 그래프가 아닌가? => 음.... 연결요소 이런거 따지는 문제도 있는거 보면 그렇게 판단하는게 옳지는 않은듯
