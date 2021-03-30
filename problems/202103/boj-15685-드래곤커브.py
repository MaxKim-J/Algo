# 접근은 잘 했는데 규칙을 이상하게 찾았음;;ㅋㅋㅋㅋㅋㅋ

import sys
input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n = int(input())
s = [[0] * 101 for i in range(101)]

# 전 세대들에 1을 더하고 뒤집어준 방향대로 간다 아니;;이거;; 넘찾기 어려운데
# 어쨋든 진행 방향을 기준으로 규칙을 찾는건 맞았다..
for i in range(n):
    y, x, d, g = map(int, input().split())
    s[x][y] = 1
    temp = [d]
    q = temp[:]
    for _ in range(g + 1):
        for k in q:
            x += dx[k]
            y += dy[k]
            s[x][y] = 1
        q = [(i + 1) % 4 for i in temp] # 대신 3에 1더하면 0이 되야 함(mod 4해서 막아주기)
        q.reverse()
        temp = temp + q

result = 0

# 이차원배열을 순회하며 점 하나를 왼쪽 상단 꼭지점으로 보고 사각형 꼴 찾기 => 이건 맞았음
for i in range(100):
        for j in range(100):
            if s[i][j] and s[i][j + 1] and s[i + 1][j] and s[i + 1][j + 1]:
                result += 1
print(result)