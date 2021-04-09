'''
이런문제는 안되면 입력이 괴랄하더라도 손디버깅이 필요한 경우가 있으니까 귀찮아 하지 말긔..
디버깅 극악 문제였다
'''

from copy import deepcopy

R, C, T = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(R)]

upper_start = upper_end = 0
downer_start = downer_end = R - 1

flag = False
for r in range(R):
  for c in range(C):
    if (board[r][c] == -1) and (not flag):
      upper_end = r
      downer_start = r + 1
      flag = True

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

def propagate():
  global board
  new_board = deepcopy(board)
  for r in range(R):
    for c in range(C):
      if board[r][c] > 0:
        value = board[r][c] // 5
        count = 0
        for i in range(4):
          nr = r + dr[i]
          nc = c + dc[i]
          if (-1 < nr < R) and (-1 < nc < C) and (board[nr][nc] != -1):
            new_board[nr][nc] += value
            count += 1
        new_board[r][c] -= (count * value)
  board = deepcopy(new_board)

def upper_clean(start, end):
  global board
  new_board = [[0] * C for _ in range(end+1)]
  for r in range(start, end + 1):
    if r == start:
      for c in range(C):
        if -1 < c - 1 < C:
          new_board[r][c-1] = board[r][c]
        else:
          new_board[r+1][c] = board[r][c]
    elif r == end:
      for c in range(C):
        if board[r][c] != -1:
          if -1 < c + 1 < C:
            new_board[r][c+1] = board[r][c]
          else:
            new_board[r-1][c] = board[r][c]
    else:
      for c in range(C):
        if c == 0:
          if board[r+1][c] != -1:
            new_board[r+1][c] = board[r][c]
          else:
           new_board[r+1][c] = -1
        elif c == C - 1:
            new_board[r-1][c] = board[r][c]
        else:
          new_board[r][c] = board[r][c]
  board = new_board[:] + board[end+1:]


def downer_clean(start, end):
  global board
  new_board = [[0] * C for _ in range(R)]
  for r in range(start, end + 1):
    if r == start:
      for c in range(C):
        if board[r][c] != -1:
          if -1 < c + 1 < C:
            new_board[r][c+1] = board[r][c]
          else:
            new_board[r+1][c] = board[r][c]
    elif r == end:
      for c in range(C):
        if -1 < c - 1 < C:
          new_board[r][c-1] = board[r][c]
        else:
          new_board[r-1][c] = board[r][c]
    else:
      for c in range(C):
        if c == 0:
          if board[r-1][c] != -1:
            new_board[r-1][c] = board[r][c]
          else:
           new_board[r-1][c] = -1
        elif c == C - 1:
            new_board[r+1][c] = board[r][c]
        else:
          new_board[r][c] = board[r][c]
  board =  board[:start] + new_board[start:]


for _ in range(T):
  propagate()
  upper_clean(upper_start, upper_end)
  downer_clean(downer_start, downer_end)

result = 0
for i in range(R):
  result += sum(board[i])

print(result + 2)

'''
from copy import deepcopy
import sys
input = sys.stdin.readline

# 확산 => 확산시키면서 만들었던 새로운 배열을 리턴
def diff():
    temp = [[0] * c for i in range(r)]
    temp[t1][t2] = -1
    temp[b1][b2] = -1
    for i in range(r):
        for j in range(c):
            if s[i][j] > 0:
                cnt = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < r and 0 <= y < c and s[x][y] != -1:
                        temp[x][y] += s[i][j] // 5
                        cnt += 1
                temp[i][j] += s[i][j] - (s[i][j] // 5 * cnt)
    return temp

# 공기청정기 부터 시작
def clar(x, y, dir):
    temp = deepcopy(s)
    cx, cy = x, y - 1
    s[x][y] = 0
    # 얘는 약간 BFS처럼 만들어줌 동서남북 체크해서 
    # x,y를 이중반복문 사이의 전역변수처럼 유지시키기
    for i in range(4):
        while True: # 이렇게하면 한쪽 방향 계속 진행 후 다른 방향으로 넘어갈 수 있음
            nx = x + dx[dir[i]]
            ny = y + dy[dir[i]]
            # 공기청정기인 경우 한바퀴 다 돌았으므로 리턴
            if nx == cx and ny == cy:
                return
            # 4방면이 격자 안일경우 방향만큼 이동한 값을 넣어줌
            if 0 <= nx < r and 0 <= ny < c:
                s[nx][ny] = temp[x][y]
            #! 격자 밖으로 간 경우 이때 xy는 그대로임 => 방향만 다르게 해서 다시 시작함(핵심)
            else:
                break 
            # 다음으로 넘어가서 계속 한 방향 반복
            x, y = nx, ny

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

r, c, t = map(int, input().split())
s = []
cl = []

for i in range(r):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(c):
        if a[j] == -1:
            cl.append([i, j])

# 공기청정기의 위치를 바탕으로 행과 열 정보 추출
t1, t2 = cl[0][0], cl[0][1]
b1, b2 = cl[1][0], cl[1][1]

for i in range(t):
    s = diff()
    # 공기청정기 위치, 방향
    #* 방향 로직이 좀 복잡할 경우에 숫자를 써서 해결하자!!!!!(아직 좀 숙련되지 않았음..)
    clar(t1, t2 + 1, [3, 1, 2, 0]) # 방향을 인자로 주는 방식으로 함수를 하나만 쓰는것도 좋은 방법
    clar(b1, b2 + 1, [3, 0, 2, 1])

s[t1][t2], s[b1][b2] = 0, 0
result = 0
for i in range(r):
    result += sum(s[i])
print(result)
'''