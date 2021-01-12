from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

# 엄밀히 말하면 약간.. unordered BFS?


def bfs():
    result = 0
    # * visit에 바로 append하는 방법과 비슷한 방법인듯
    # 어쨋든 같은 뎁스에서 노드들을 순회하는 건데
    queue = set()
    queue.add((0, 0, board[0][0]))
    while queue:
        x, y, sentence = queue.pop()
        result = max(result, len(sentence))
        # 알파벳을 모두 한번씩 지나면 땡이므로
        #! 사실 나올 수 있는 최대 암호 자리는 26, 트리의 최대 뎁쓰도 26
        if result == 26:
            return 26
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 바로 그냥 암호에 있는지 없는지 판단함. visit을 따로 둘 필요가 없으나
            # 다만 큐에 들어가있는 상태의 노드라면 visit을 할 필요가 없어짐
            if (-1 < nx < R) and (-1 < ny < C) and (board[nx][ny] not in sentence):
                queue.add((nx, ny, sentence + board[nx][ny]))
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
            num = to_num(nx, ny)
            if c[num] == 0:
                c[num] = 1
                dfs(nx, ny, cnt+1)
                c[num] = 0

# 알파벳 0부터 시작하는 유니코드 체계
def to_num(x, y):
    return ord(a[x][y]) - ord('A')

m, n = map(int, input().split())
a = [list(map(str, input().strip())) for _ in range(m)]
c, ans = [0]*26, 0

c[to_num(0, 0)] = 1
dfs(0, 0, 1)
print(ans)
'''
