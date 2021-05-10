dr = (0,0,1,-1)
dc = (1,-1,0,0)

N = int(input())
board = [[0]*N for _ in range(N)]
fav_friend = [0] + [0]*(N**2)

def get_pos(result):
  ultimate = list(sorted(result, key=lambda x:(-x[0], -x[1], x[2], x[3])))
  return (ultimate[0][2], ultimate[0][3])

for _ in range(N**2):
  student, *friends = map(int, input().split())
  fav_friend[student] = friends
  result = []
  for r in range(N):
    for c in range(N):
      favorite, close = 0, 0
      if board[r][c] == 0:
        for i in range(4):
          nr = r + dr[i]
          nc = c + dc[i]
          if -1 < nr < N and -1 < nc < N:
            if board[nr][nc] in friends:
              favorite += 1
            if board[nr][nc] == 0:
              close += 1
        result.append([favorite, close, r, c])

  pos_r, pos_c = get_pos(result)
  board[pos_r][pos_c] = student

ans = 0

for r in range(N):
  for c in range(N):
    count = 0
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if -1<nr<N and -1<nc<N:
        if board[nr][nc] in fav_friend[board[r][c]]:
          count += 1
    ans += 0 if count == 0 else 10**(count-1)

print(ans)