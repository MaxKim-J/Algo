from itertools import combinations
 
## 맵크기(N), 치킨집 최대 선택가능개수(M)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
 
## 빈칸(0), 집(1), 치킨집(2)
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1: house.append((i, j))
        elif board[i][j] == 2: chicken.append((i, j))
 
minv = float('inf')
for ch in combinations(chicken, M):
    sumv = 0
    for home in house:
        # 어;;;;;;; 그러네 치킨집 좌표 아니까 Min만 해주면 되자나 ㅋㅋㅋㅋ
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        # 계속 더하다가도 그동안 도출했던 값을 넘으면 거기서 멈춤 더이상 계산할 필요 없음
        if minv <= sumv: 
          break
    if sumv < minv: 
      minv = sumv
 
print(minv)


'''
개에바 시간에 돌았던 내 코드;;(BFS) Pypy에서는 돌았음
직접 치킨집까지 가야할 당위가 있었다면 이렇게도 풀렸을듯 하다


from itertools import combinations
from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def get_chicken_distance(board, sr, sc):
  queue = deque([(sr, sc)])
  visited = [[0] * (n+1) for _ in range(n+1)]
  visited[sr][sc] = 1
  while queue:
    r, c = queue.popleft()
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if 0 < nr <= n and 0 < nc <= n and visited[nr][nc] != 1:
        visited[nr][nc] = 1
        if board[nr][nc] == 2:
          return (abs(sr - nr) + abs(sc - nc))
        else:
          queue.append((nr, nc))


n, m = map(int, input().split())
board = [[0] * (n + 1)]
for _ in range(n):
  board.append([0] + list(map(int, input().split())))

chickens = []
houses = []

for r in range(n+1):
  for c in range(n+1):
    if board[r][c] == 2:
      chickens.append((r,c))
      board[r][c] = 0
    elif board[r][c] == 1:
      houses.append((r,c))

alive_chickens = list(combinations(chickens, m))

result = 10000

for chickens in alive_chickens:
  for r, c in chickens:
    board[r][c] = 2
  chicken_distance = 0
  for sr, sc in houses:
    chicken_distance += get_chicken_distance(board, sr, sc)
  result = min(result, chicken_distance)
  for r,c in chickens:
    board[r][c] = 0

print(result)
'''