from math import floor

'''
문제 이해가 잘 안되었음 => 한 칸에서 벌어지는 일이라고 해놓고
하나로 합쳐지고 4개로 분리되는데 방향이 어쩌구 저쩌고 너무 복잡하게 써놓은듯;
행간을 좀 더 꼼꼼히 봐야 할 필요는 있음. 진짜 나중에 실전에서 이해가 안될때
근거를 찾아서 그 방향대로 풀어야함
'''

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

def move():
  global board
  #* 결과를 어떻게 기록해야 무결하고 가장 좋을지 계속 생각하자
  current = [[[] for _ in range(N)] for _ in range(N)]
  for r in range(N):
    for c in range(N):
      if len(board[r][c]):
        for cm, cs, cd in board[r][c]:
          nr = (r + dr[cd] * cs) % N
          nc = (c + dc[cd] * cs) % N
          current[nr][nc].append((cm, cs, cd))
  board = current

def spawn():
  global board
  for r in range(N):
    for c in range(N):
      count = len(board[r][c])
      if count > 1:
        subs = set()
        sum_m, sum_s = 0, 0
        for cm, cs, cd in board[r][c]:
          sum_m += cm
          sum_s += cs
          subs.add(cd % 2)
        new_fire = []
        new_fire_m = floor(sum_m/5)

        if len(subs) == 1:
          for i in range(8):
            if i % 2 == 0:
              new_fire.append((new_fire_m, floor(sum_s/count), i))
        else:
          for i in range(8):
            if i % 2 == 1:
              new_fire.append((new_fire_m, floor(sum_s/count), i))

        if new_fire_m > 0:
          board[r][c] = new_fire
        else:
          board[r][c] = []

for _ in range(M):
  r, c, m, s, d = map(int, input().split())
  board[r-1][c-1].append((m,s,d))

for _ in range(K):
  move()
  spawn()

result = 0
for r in range(N):
  for c in range(N):
    if len(board[r][c]):
      for fire in board[r][c]:
        result += fire[0]

print(result)
