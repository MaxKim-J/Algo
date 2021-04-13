import sys
#* 이거 너무너무 잘풀었다

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 꼭 조건을 나누려고 하지 않고 자연스러운 흐름에서 문제가 풀린듯
# 공통점을 찾아내고, 공통된 연산은 미리 해보기
def move(chess_num):
    # 걍 바로찾아버리기
    x, y, z = chess[chess_num]

    # 기본적인 새 위치
    nx = x + dx[z]
    ny = y + dy[z]

    # 파 : 파 > 파 일경우 처리
    if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
        # 반대방향 도출
        if 0 <= z <= 1:
            nz = (z+1) % 2
        else:
            nz = (z-1) % 2 + 2
        # 재귀를 써서 머리아플 필요 없었다.. 그냥 한번만 더 해주면 됐었음(간단한 케이스인지 생각해보자)
        chess[chess_num][2] = nz

        # 파랑에서 다시 들어온 경우 새로운 위치
        nx = x + dx[nz]
        ny = y + dy[nz]

        # 파랑을 만난 후 한번 더 만나는게 아니면 여길 빠져나옴
        if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
            return 0

    chess_set = []

    # 흰/빨
    # 있는 것들 순회
    for i, key in enumerate(chess_map[x][y]):
        # 그중에 인덱스와 같다면 chess set에 일단 잘라서 이동을 시켜줌
        # 이때 원래 있던 말도 포함이 됨
        if key == chess_num:
            chess_set.extend(chess_map[x][y][i:])
            chess_map[x][y] = chess_map[x][y][:i] # 일단 초기화
            break

    # 빨강이면 한번 뒤집어줌
    if a[nx][ny] == 1:
        chess_set = chess_set[-1::-1]

    # 적용. chess set에 있는거 순회하면서 chessMap과 chess를 업데이트
    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx, ny]

    if len(chess_map[nx][ny]) >= 4:
        return 1
    return 0

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 연동되는 자료구조 사용 => 3차원배열을 매번 까뒤집는게 쉬운 일은 아니다
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]

for i in range(k):
    x, y, z = map(int, input().split())
    #! 이게 ㄹㅇ 핵심. 삼차원 이상의 배열은 연산이 어렵지 않을때만 간단히 쓰자
    # 자료를 쉽게 조회할 수 있는 구조를 생각해내자.
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z-1]

# cnt 정해서 단순화하기
cnt = 1
while cnt <= 1000:
    # 이렇게 단순화해놓으면 매번 번호만 순회하면 OK가 된다...
    for i in range(k):
        flag = move(i)
        # 옮기다가 4가 되었을 경우 1을 리턴
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)

'''
단순화해서 풀자!!!!!! 너무 길게 돌아간다 항상..
함수 3개, 코드 80줄 이상은 왠만한 문제에는 필요없을듯 디버깅도 못함 어차피...
처음부터 최적화된 방법과 가장 가까운 방법을 생각할 수 있어야 풀 수 있음 => 
스켈레톤을 다 쓰지 말자. 구조 + 한국말로만 잡고 계속 검증한 뒤에 코딩해보기

N, K = map(int, input().split())
board = [input().split() for _ in range(N)]
game = [[[] for _ in range(N)] for _ in range(N)]


for i in range(K):
  sr, sc, d = map(int, input().split())
  game[sr-1][sc-1].append([i + 1, d])

print(game)

dr = (0,0,0,-1,1)
dc = (0,1,-1,0,0)

def opposite_dir(direction):
  return direction - 1 if direction % 2 == 0 else direction + 1

def go(r, c, nr, nc, j, dir, chance):
  if not(-1 < nr < N) or not(-1 < nc < N) or (board[nr][nc] == '2'):
    if chance == 1:
      new_dir = opposite_dir(dir)
      game[r][c][j][1] = new_dir
      go(r, c, r + dr[new_dir], c + dc[new_dir], j, new_dir, 2)
    else:
      return
  elif board[nr][nc] == '0':
    game[nr][nc] += game[r][c][j:]
    game[r][c] = game[r][c][:j]
  elif board[nr][nc] == '1':
    game[nr][nc] += list(reversed(game[r][c][j:]))
    game[r][c] = game[r][c][:j]

def process(turn, pointer):
  for r in range(N):
    for c in range(N):
      for j in range(len(game[r][c])):
        current = game[r][c][j]
        if current[0] == pointer:
          nr = r + dr[current[1]]
          nc = c + dc[current[1]]
          print(current, nr,nc)
          go(r, c, nr, nc, j, current[1], 1)
          print(game[nr][nc])
          if len(game[r][c]) == 4:
            print(turn)
            exit(0)
          return True
  
def solve(game):
  turn = 1
  while True:
    pointer = 1
    while pointer < K + 1:
      if process(turn, pointer):
        pointer += 1
    turn += 1
    print(game)
    print(turn)
    if turn > 10:
      return -1

print(solve(game))
'''