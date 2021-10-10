from collections import deque

'''
접근은 맞았는데 문제의 조건이 명확하지 못해서 헷갈린 부분이 있었고
세부 조건을 제대로 설정하지 못해서 시간이 좀 더 걸렸다

일단 거울이 45도 틀어졌다는데 시계방향인지 아닌지 둘 다인지 정확한 언급이 없어서 해맴
그리고 방과 벽과 문의 조건이 제대로 제시되지 않아서 벽이 없는 방도 가능할지 몰랐음..
일자로 탐색할때 벽을 만나면 끝나야하는데 고려하지 않음

질문에서 테케를 더 찾아보고 돌리니까 답이 잘 나왔다. 반례를 스스로 공급하자!
'''

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# 거울의 방향전환 Rule
def change_d(d):
  if d == 2 : return [1,3]
  elif d == 3 : return [2,0]
  elif d == 0 : return [1,3]
  elif d == 1 : return [2,0]

def straight_BFS(sr, sc, starts, n, tr, tc):
  queue = deque([(sr, sc, start, 0) for start in starts])
  while queue:
    r, c, d, depth = queue.popleft()
    for i in range(1, n):
      nr = r + (dr[d] * i)
      nc = c + (dc[d] * i)
      if -1 < nr < n and -1 < nc < n:
        if board[nr][nc] == '!':
          for new_d in change_d(d):
            queue.append((nr, nc, new_d, depth+1))
        elif board[nr][nc] == '#' and nr == tr and nc == tc:
          return depth
        elif board[nr][nc] == '*':
          break

# 입력 받기
N = int(input())
board = []
door = []

# 문 위치 파악
for i in range(N):
  row = list(input())
  for j in range(N):
    if row[j] == '#':
      door.append((i,j))
  board.append(row)

# 시작 문에서 어디로 출발할 수 있는지 파악
sr, sc = door[0]
starts = []

for i in range(4):
  nr = sr + dr[i]
  nc = sc + dc[i]
  if -1 < nr < N and -1 < nc < N and board[nr][nc] != '*':
    starts.append(i)

answer = straight_BFS(sr, sc, starts, N, door[1][0], door[1][1])
print(answer)