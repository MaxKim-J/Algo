
from collections import deque
import sys
# 탑다운으로 

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    xcnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny < 0:
                ny = m-1
            elif ny > m-1:
                ny = 0

            if 0 <= nx < n and 0 <= ny < m and not c[nx][ny]:
                # 인접한 묶음의 개수만 구한다
                if a[x][y] == a[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])
                    xcnt += 1

    return xcnt

n, m, t = map(int, input().split())

a, nsum, nm = [], 0, n*m

# 일단 모두 더하고 시작
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    nsum += sum(row)

q = deque()
c = [[0]*m for _ in range(n)] # visited

for _ in range(t):
    x, d, k = map(int, input().split())
    # 어짜피 돌고도는거라 mod 해도 똑같

    k %= m
    # 회전 => for문 돌릴필요 없이 mod를 사용하면 어디를 때줘야하는지 정해줄 수 있음
    for i in range(x-1, n, x):
        if d == 0:
            a[i] = a[i][-k:] + a[i][:-k]
            c[i] = c[i][-k:] + c[i][:-k]
        else:
            a[i] = a[i][k:] + a[i][:k]
            c[i] = c[i][k:] + c[i][:k]

    flag = 0
    for i in range(n):
        for j in range(m):
            if not c[i][j]:
                # 인접한 것들의 개수만 리턴 => board를 직접 바꾸지 않았다
                #! 이렇게 하면 묶음 나오는거 맞으니까 쫄지말구...
                cnt = bfs(i, j)
                # 인접한 수들이 있다면
                if cnt:
                    nsum -= a[i][j] * cnt   # 전체에서 빼주고(걍 합에서 없애줌)
                    nm -= cnt # 숫자 개수만큼 또 빼줌
                    flag = 1

    # 숫자가 아무것도 안남고 모두 사라졌을때 
    if nm == 0:
        print(0)
        sys.exit()

    if not flag:
        #! 평균, 파이썬은 float과 int사이의 비교연산이 가능하다
        avg = nsum / nm
        for i in range(n):
            for j in range(m):
                if not c[i][j]:
                    if a[i][j] > avg:
                        a[i][j] -= 1
                        nsum -= 1 # 전체에서도 연산한다
                    elif a[i][j] < avg:
                        a[i][j] += 1
                        nsum += 1

# 결국 답은 합이었기때문에 정답 지향적으로 푸는 방법이 되었다..
print(nsum)

'''
시간초과

- 백트랙킹 없이 매번 완전탐색을 해서 그런거같음...
- 코드에 군더더기가 너무 많다 최적화를 시켜주자!! 정답지향적으로 풀기,,
- 군더더기가 너무 많은 것은, 모든 과정을 다 구현하는 방식으로 풀기 때문
- 코드에 신경쓰지 말고 답을 해결해나가는 과정을 생각해내는데 집중하자.

from copy import deepcopy

dr = (0,0,1,-1)
dc = (1,-1,0,0)

N, M, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def turn(x, d, k):
  for r in range(x - 1, N, x):
    for _ in range(k):
      new_line = [board[r][-1]] + board[r][:-1] if d == 0 else board[r][1:] + [board[r][0]]
      board[r] = new_line

def DFS(r, c, n, visited):
  global flag
  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if (i == 0) and (M <= nc):
      nc = 0
    if (i == 1) and (nc < 0):
      nc = M - 1
    if (-1 < nr < N) and (-1 < nc < M):
      if (board[nr][nc] != -1) and (visited[nr][nc] != -1):
        visited[nr][nc] = -1
        if n == board[nr][nc]:
          board[r][c] = -1
          DFS(nr, nc, board[nr][nc], visited)
          board[nr][nc] = -1
          flag = True

for _ in range(T):
  x, d, k = map(int, input().split())
  turn(x,d,k)
  flag = False
  count = total = 0
  for r in range(N):
    for c in range(M):
      visited = deepcopy(board)
      if board[r][c] != -1:
        count += 1
        total += board[r][c]
        DFS(r,c, board[r][c], visited)

  if not flag:
    average = total / count
    for r in range(N):
      for c in range(M):
        if board[r][c] != -1:
          if board[r][c] > average:
            board[r][c] -= 1
          elif board[r][c] < average:
            board[r][c] += 1

result = 0

for r in range(N):
  for c in range(M):
    if board[r][c] != -1:
      result += board[r][c]

print(result)
'''