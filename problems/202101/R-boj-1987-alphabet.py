# BFS, DFS, 단순 백트랙킹 등 백트랙킹을 하는 모든 방법으로 풀 수 있다
# 탐색을 하는데 있어서 뭐 꼭 그래프순회식으로 할 필요는 없다

from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

# 엄밀히 말하면 약간.. unordered BFS?
# 이문제는 BFS로 하는게 성능이 월등히 좋았음


def bfs():
    result = 0
    # * visit에 바로 append하는 방법과 비슷한 방법인듯
    # 어쨋든 같은 뎁스에서 노드들을 순회하는 건데
    # 이런식으로도 백트랙킹이 가능함
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
            # 어짜피 글자가 같으니까 다 탐색 했을때는 중복으로 경우의 수가새지는거임
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
            # 재귀 DFS는 처음 visit을 표기해놓고, 재귀를 돌려서 다음 depth의 노드로 바로 들어가는데
            if c[num] == 0:
                c[num] = 1
                dfs(nx, ny, cnt+1)
                # 그 노드 탐색이 끝나면 visit을 원복시킴 그럼 아래 뎁스의 다음 노드 탐색
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

'''
백트랙킹 풀이

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


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())  # R, C | 세로, 가로
words = [list(input()) for _ in range(n)]
result = 0
backt(0, 0, words[0][0])
print(result)
'''
