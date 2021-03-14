'''
백준 2186번 <문자판>

어렵다 진짜 그리고 사실상 DP문제였음

1. N과 M 테스트 케이스가 필요했다
2. 스켈레톤 구현한 부분마다 확실한 검증이 필요하다
3. 일단 너무 예쁘게 구현하려고 생각하지 않아야 할거같음
4. 아무리 생각해도 삼차원 배열은 에바다... enable_node를 제하더라도 문자열로 바꿔서 풀자
5. BFS로는 시간초과 DP로는 풀림
'''
from collections import deque

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def dfs(y, x, idx):
    print(y,x, idx)
    if idx == len(word):
        return 1
    # 이미 방문한 곳 + 이미 방문한 인덱스라면 그 자체를 리턴한다
	# idx는 해당 칸을 방문했을 때 전체 단어에서 몇번째 방문인지를 기록함. 거기를 이미 방문했다는 것은
	# 거기서부터는 다시 이하 낱자를 찾아간 것을 그대로 백트랙킹 할 수 있다는 것임(똑같이 사용 가능)
    #! 그 칸을 n번째 낱자를 완성하기 위해 방문했음. 그리고 C는 거기서부터 시작할때 완성된 낱자를 만들 수 있는 경우의 수를 DFS로 모두 구함
    if c[y][x][idx] != -1:
        return c[y][x][idx]

    c[y][x][idx] = 0
    for i in range(4):
        temp_y, temp_x = y, x
        for _ in range(k):
            ny = temp_y + dy[i]
            nx = temp_x + dx[i]
            if 0<= ny< n and 0<=nx < m:
                if a[ny][nx] == word[idx]:
                    c[y][x][idx] += dfs(ny, nx, idx+1)
            temp_y, temp_x = ny, nx
    return c[y][x][idx]


n, m, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input().strip()))
word = list(input().strip())

start = []
# dfs 후보들을 고른다
for i in range(n):
    for j in range(m):
        if a[i][j]==word[0]:
            start.append([i,j])

ans = 0
c = [[[-1]*len(word) for _ in range(m)] for _ in range(n)]
for i in range(len(start)):
    y, x = start[i]
    ans += dfs(y, x, 1)

print(ans)