N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

clouds = [(N-1,0), (N-1,1), (N-2,0), (N-2,1)]

# 인덱스 하나 빼서 참조시키기
dr = (0, -1, -1, -1, 0, 1, 1, 1)
dc = (-1, -1, 0, 1, 1, 1, 0, -1)

def move(d, s):
  global clouds, board
  new_clouds = []
  for r,c in clouds:
    # 짜피 s가 정해져 있으니 그칸으로 바로 가면 됨
    nr = r + (dr[d-1] * s)
    nc = c + (dc[d-1] * s)
    # 격자 밖으로 나갔을때 연결시킨 칸으로 이동시키기
    if nr < 0:
      nr = N - ((-nr) % N) if (-nr) % N > 0 else 0
    if nc < 0:
      nc =  N - ((-nc) % N) if (-nc) % N > 0 else 0

    if nr > N-1:
      nr = nr % N
    if nc > N-1:
      nc = nc % N
    # 순차적으로 계속 진행해도 되는 부분인듯
    new_clouds.append((nr, nc))
    board[nr][nc] += 1
  clouds = new_clouds[:]
    
def copy_water():
  # 전 단계에서 물이 증가한 칸
  global clouds, board
  # 대각선 방향 순회하여 물이 있는지 체크, 
  for r, c in clouds:
    count = 0
    # 이때 dr, dc의 홀수번째 인덱스만 이용하면 됨
    for i in range(1, 8, 2):
      nr = r + dr[i]
      nc = c + dc[i]
      if (-1<nr<N) and (-1<nc<N) and (board[nr][nc] > 0):
        count += 1
    board[r][c] += count


def make_cloud():
  # 전전 단계에서 구름이 사라진 칸
  global clouds, board
  new_clouds = []
  for r in range(N):
    for c in range(N):
      if (board[r][c] >= 2) and ((r,c) not in clouds):
        board[r][c] -= 2
        new_clouds.append((r,c))
  clouds = new_clouds[:]

for u in range(M):
  d, s = map(int, input().split())
  move(d, s)
  copy_water()
  make_cloud()

result = 0
for i in range(N):
  result += sum(board[i])

print(result)
