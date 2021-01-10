'''
백준 5014 <스타트링크>

문제 핵심 : 업 다운 버튼을 눌러서 갈 수 있는 층의 경우의 수를 순회해서 버튼을 눌러야 하는 최솟값을 찾는다

연산 계산 : 
  1. depth가 최대 100만개이고 트리가 이진트리(업, 다운)이므로 완전탐색시 2**100만의 간선이 최대로 존재할 수 있음
  2. 너무 많기 때문에 중복되는 서브트리를 제외하는 백트랙킹을 통해 최대 층수개 만큼의 노드를 방문하면 된다
  3. 따라서 간선의 개수는 층수가 n개일때 (층수 * 2) 즉 O(2n) => 1초 안에 해결이 가능하다
핵심 아이디어 : 
  1. visit했다면 경우의 수를 보존할 필요가 없으므로 queue append와 동시에 visit append를 실행한다
  2. 큐에는 depth와 노드의 값이 들어가면 된다
'''


from collections import deque

F, S, G, U, D = map(int, input().split())


def BFS(start, goal):
    visited = [False] * (F + 1)
    queue = deque([(start, 0)])

    while queue:
        current, depth = queue.popleft()
        if current == goal:
            return depth
        if (current + U <= F) and (not visited[current + U]):
            queue.append((current + U, depth + 1))
            visited[current + U] = True
        if (current - D > 0) and (not visited[current - D]):
            queue.append((current - D, depth + 1))
            visited[current - D] = True
    return 'use the stairs'


print(BFS(S, G))
