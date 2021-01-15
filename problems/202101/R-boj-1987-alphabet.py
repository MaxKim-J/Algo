'''
백준 1987 알파벳

- 이 문제는 BFS, DFS, 단순 백트랙킹 등 백트랙킹을 하는 모든 방법으로 풀 수 있다
- 탐색을 하는데 있어서 항상 뭐 꼭 그래프 순회식으로 할 필요는 없다
- 이 문제는 BFS로 하는게 성능이 월등히 좋았음 => 최적 depth는 일단 BFS로 가자구
- 연산 : 참 이게 백트랙킹 했을 때의 경우의 수를 생각해내기가 힘듬
    - 최대 문자판의 크기 20*20이고 최악의 경우 모든 칸(400개) 다 방문할 수 있을 때 가장 많은 연산을 할 것
    - 대충 4방향으로 다 갈 수 있다고 생각하면 4 + 4**2 + 4**3 + ... + 4**400 => 완전탐색으로는 힘들고 백트랙킹 필요
    - 백트랙킹을 했을 경우 : 이미 갔던 알파벳은 순회하지 않으므로, 알파벳에 시간복잡도가 의존하게 됨
    - 백트랙킹 방법 : 알파벳은 총 26개이므로 최대 depth는 26(4^26) + 그리고 경계 근처의 칸에서는 4가 아니라 3, 2개의 순회 가능
    - 이런 꼴일때는 시간복잡도를 정확하게 측정하기 어렵긴 하다 입력의 유형에 따라 천차만별이라서
    - 여기까지 생각하고 대충 많이 줄겠군 + 어떻게 해야 답에 빨리 도달하겠군 => BFS, DFS, 재귀 백트랙킹 중 편한 방법으로 + DP
'''


from collections import deque

# 동서남북은 이렇게 하는게 뭔가 직관적인듯
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def bfs():
    result = 0
    queue = deque([(0, 0, board[0][0])])
    visited = dict()
    while queue:
        x, y, sentence = queue.popleft()
        result = max(result, len(sentence))
        if result == 26:
            return 26
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (-1 < nx < R) and (-1 < ny < C) and (board[nx][ny] not in sentence):
                # x,y,value가 같은 노드는 단 한번만 돌면 된다(위 value까지 다 같다는 뜻이므로)
                #! 무슨 값일때 또한번 돌아야 하는지 생각해볼것(BFS할때는)
                current = (nx, ny, sentence + board[nx][ny])
                if not visited.get(current):
                    queue.append(current)
                    visited[current] = 1
    return result


R, C = map(int, input().split())
board = [input() for _ in range(R)]
print(bfs())

'''
정석? 적인 풀이 : DFS + ORD 사용하여 유니코드로 바꾸기
이게 더 단순해보이긴 함
약간 depth가 정해져있는 상황에선 재귀로 구현하는 DFS가 구현하기는 좀더 괜찮은 방법일수도있음

import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 재귀 DFS...외울것
def dfs(x, y, cnt):
    global ans
    if cnt == 26:
        ans = 26
        return
    else:
        ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            # 재귀 DFS는 방문한 노드가 아닐때 그 노드의 leap를 향해서 계속 감
            num = to_num(nx, ny)
            if c[num] == 0:
                c[num] = 1
                dfs(nx, ny, cnt+1)
                # 그 노드 깊이 탐색이 끝나면 visit을 원복시킴 그럼 아래 뎁스의 다음 노드 탐색 (i++)
                c[num] = 0

# 알파벳 0부터 시작하는 유니코드 체계 => visit배열로 구현
def to_num(x, y):
    return ord(a[x][y]) - ord('A')

m, n = map(int, input().split())
a = [list(map(str, input().strip())) for _ in range(m)]
c, ans = [0]*26, 0

c[to_num(0, 0)] = 1
dfs(0, 0, 1)
print(ans)
'''

'''
백트랙킹 풀이 => 걍 단순하게는 이렇게도 된다
굉장히 쉽고 직관적인 풀이가 되었다

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def backt(x, y, word):
    global result
    check = 0
    for k in range(4):  # 상 하 좌 우 4방향 탐색
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and words[nx][ny] not in word:  # 인덱스 초과 방지 & 문자 중복 방지
            backt(nx, ny, word+words[nx][ny])
        else:
            check += 1

    # 더 이상 이동할 수 없으면 문자의 길이를 확인해 준다.
    if check == 4:
        result = max(result, len(word))
        return


n, m = map(int, input().split())  # R, C | 세로, 가로
words = [list(input()) for _ in range(n)]
result = 0
backt(0, 0, words[0][0])
print(result)
'''
