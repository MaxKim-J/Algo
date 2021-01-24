from collections import deque

# * DFS, BFS 레벨에서 백트랙킹을 해도 시간초과가 뜬다면 다른 방법이 필요하다
#! 여기서는 visited를 이용한 자연스러운 DP, 그리고 큐 추가하는 순서를 조작하는 태크닉을 적용

# M, N = map(int, input().split())
# board = [tuple(input()) for i in range(N)]

M = 6
N = 6
board = [
    ['0', '0', '1', '1', '1', '1'],
    ['0', '1', '0', '0', '0', '0'],
    ['0', '0', '1', '1', '1', '1'],
    ['1', '1', '0', '0', '0', '1'],
    ['0', '1', '1', '0', '1', '0'],
    ['1', '0', '0', '0', '1', '0'],
]

update_c = [0, 0, 1, -1]
update_r = [1, -1, 0, 0]

# 결과를 기록하는 동시에 visited여부를 파악할 수 있어 메모리 절약 가능(DP)
#! BFS로 경로를 찾아내는 문제에서, 큐에 depth를 같이 저장하는 방식보다 visited를 이용하면 좀더 효율적인 풀이가 가능하다
dist = [[-1]*M for _ in range(N)]


def BFS(start_r, start_c):
    global dist
    queue = deque([(start_r, start_c)])
    dist[start_r][start_c] = 0
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            new_c, new_r = c + update_c[i], r + update_r[i]
            # 아직 방문하지 않는 얘들 방문(짜피 최단 벽뿌경로)
            if (-1 < new_c < M) and (-1 < new_r < N) and dist[new_r][new_c] == -1:
                # 모든 경로를 탐색하는 것은 달라지지 않는다 + 각 노드는 한번만 방문
                # 다만 방문한 칸 값이 무엇인지에 따라 큐에 추가하는 방법이 다른데
                #! 0일 경우 dist를 올리지 않기 때문에 우선해서 탐색을 진행하는 방식으로 백트랙킹을 해줄 수 있는 것이다.
                # * 가장 적은 비용에 대한 탐색이 끝나고 나서야 비로소 더 큰 비용의 경로를 탐색한다
                # * 어떻게 하면 답에 가장 빨리 접근할 수 있냐? 에 대한 답
                # * dist 배열에서는 해당 칸에 도달했을때까지의 최소 벽깨기 개수 저장 => 다익스트라 맞네..
                if board[new_r][new_c] == '0':
                    queue.appendleft((new_r, new_c))
                    dist[new_r][new_c] = dist[r][c]
                elif board[new_r][new_c] == '1':
                    queue.append((new_r, new_c))
                    dist[new_r][new_c] = dist[r][c] + 1


BFS(0, 0)
# 저런 백트랙킹을 사용하면 마지막 찾고자하는 칸의 dist에는 최소경로가 저장된다
print(dist)
print(dist[M-1][N-1])

# 연관문제 = 2186 문자판

'''
시간초과난 BFS => 자체로 할 수 있는 백트랙킹보다 좀 더 가지를 쳐낼 수 있는 이상의 방법이 필요했던 것
다익스트라로도 풀수 있는듯 하다

def BFS(start_r, start_c):
    global result
    visited = {}
    queue = deque([(start_r, start_c, 0)])
    while queue:
        r, c, count = queue.popleft()
        if (r == N-1 and c == M-1):
            result = min(result, count)
            continue
        if count >= result:
            continue
        for i in range(4):
            new_c = c + update_c[i]
            new_r = r + update_r[i]
            if (-1 < new_c < M) and (-1 < new_r < N) and not visited.get((new_r, new_c, count)):
                current = (new_r, new_c, count +
                           1 if board[new_r][new_c] == 1 else count)
                queue.append(current)
                visited[current] = True
'''
