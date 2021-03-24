n, m = map(int, input().split())
R,C,d = map(int, input().split())

board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_direction(direction):
  if direction == 0:
    return [3, 2, 1, 0]
  elif direction == 1:
    return [0, 3, 2, 1]
  elif direction == 2:
    return [1, 0, 3, 2]
  elif direction == 3:
    return [2, 1, 0, 3]


def clean(ir, ic, id):
  global count
  r, c, d = ir, ic, id

  while True:
    print(r,c,d)
    if board[r][c] == 0:
      board[r][c] = 2
      count += 1
    flag = 0
    for nd in get_direction(d):
      nr = r + dr[nd]
      nc = c + dc[nd]

      if -1 < nr < n and -1 < nc < m:
        if board[nr][nc] == 0:
          r, c, d = nr, nc, nd
          break
        else:
          flag += 1
        
    # 후진
    if flag == 4:
      nd = d - 2 if d > 1 else d + 2
      pr = r + dr[nd]
      pc = c + dc[nd]

      if board[pr][pc] != 1:
        r, c, d = pr, pc, d
      else:
        return

count = 0
clean(R, C, d)
print(count)

'''
요게 좀더 직관적인 풀이,,

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 방향 바꿔주기
def change(d):
    if(d == 0):
        return 3
    elif(d == 1):
        return 0
    elif(d == 2):
        return 1
    elif(d == 3):
        return 2

def find(r,c,d):
    cnt = 1
    x = r
    y = c
    arr[x][y] = 2 
    while(True):
        dc = d
        for i in range(4):
            empty = 0
            dc = change(dc)
            nx = x + dx[dc]
            ny = y + dy[dc]
            # 유효 범위 안에 있고, 빈칸이라면
            if(0<=nx<n and 0<=ny<m and arr[nx][ny] == 0):
                cnt += 1
                x = nx
                y = ny
                arr[nx][ny] = 2
                d = dc
                empty = 1
                break
        # 4방향 모두 탐색 후 모든 칸이 청소가 되었다면
        if(empty == 0):
            # 후진
            if(d == 0):
                x += 1
            elif(d == 1):
                y -= 1
            elif(d == 2):
                x -= 1
            elif(d == 3):
                y += 1
            # 후진하려는 칸이 벽이라면 stop
            if(arr[x][y] == 1):
                break
    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = find(r,c,d)
print(res)
'''