from collections import deque;

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = (0,0,1,-1)
dc = (1,-1,0,0)

def BFS(sr, sc, visited):
  queue = deque([(sr, sc)])
  visited[sr][sc] = 1
  block = board[sr][sc]
  group = [(sr, sc)]
  rb = 1 if board[sr][sc] == 0 else 0
  while queue:
    r, c = queue.popleft()
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if (-1 < nr < N) and (-1 < nc < N) and (visited[nr][nc] == 0):
        #! 무지개를 세어준다
        if board[nr][nc] == 0:
          rb += 1
        # 인접한 블럭이 시작점과 같은 블럭이거나 무지개라면 그룹 가능
        if (board[nr][nc] == block) or (board[nr][nc] == 0):
          visited[nr][nc] = 1
          queue.append((nr, nc))
          group.append((nr, nc))

  #! 기준 블록을 규명한다
  sp = list(sorted(group, key=lambda x:(x[0], x[1])))[0]
  return (group, rb, sp[0], sp[1])

def get_big_group():
  visited = [[0] * N for _ in range(N)]
  groups = []
  for r in range(N):
    for c in range(N):      
      if (visited[r][c] == 0) and (board[r][c] > 0):
        group_info = BFS(r, c, visited)
        if (len(group_info[0]) >= 2):
          groups.append(group_info)

  # 그룹이 하나도 없는경우 예외처리
  if len(groups) == 0:
    return False

  # 기준에 따라 가장 큰 그룹 구하기
  big_group = list(sorted(groups, key=lambda x:(-len(x[0]), -x[1], -x[2], -x[3])))[0][0]

  # 빅그룹 제거 => -2가 빈칸
  for r, c in big_group:
    board[r][c] = -2

  # 더할 점수 리턴
  return len(big_group) ** 2

def gravity():
  global board
  # 차례대로 빈칸을 순회함
  for r in range(N):
    for c in range(N):
      if board[r][c] == -2:
        # 현재의 행보다 위에 있는 것은 모두 바라봄
        for i in range(r, 0, -1):
          # 빈칸 위 어드매에 있는 블럭이 무지개블럭이거나 일반 블럭이라면
          if board[i-1][c] > -1:
            # 끌어내림(빈칸과 바꿔치기)
            board[i][c], board[i-1][c] = board[i-1][c], board[i][c]
          else:
            break

def rotate():
  global board
  new_board = [[-3]*N for _ in range(N)]
  # 위에부터 행이 같은번호 열로, 요소를 반대로 해서 이동함
  for i in range(N):
    for j in range(N):
      new_board[j][i] = board[i][(N-1)-j]

  # 새로운 배열을 기존 배열과 치환
  board = new_board

score = 0

while True:
  turn_score = get_big_group()
  if turn_score:
    score += turn_score
  else:
    print(score)
    break
  gravity()
  rotate()
  gravity()