import sys
from copy import deepcopy

input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

#! 상어가 먹는 모든 경우의 수를 대상으로 그래프순회 => 그리디라고 속단하지 말자.,,,
def dfs(x, y, d, cnt):
    global ans, a, fish
    # DFS를 하는 과정에서 move fish를 매번 해주기
    move_fish(x, y)
    #* for i in range(4) 해도 된다고 생각함
    while True:
        nx, ny = x + dx[d], y + dy[d]
        # 같은 방향에서 여러번 탐색하며 물고기를 찾았음에도 격자에서 나간 경우 => 상어가 갈 곳이 없음 => 리턴
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            ans = max(ans, cnt)
            return
        # 물고기가 없는 경우 => 뛰어넘기(상어는 여러칸 갈 수 있음)
        if not a[nx][ny]:
            x, y = nx, ny
            continue

        # 기록
        temp_a, temp_fish = deepcopy(a), deepcopy(fish)
        temp1, temp2 = fish[a[nx][ny][0]], a[nx][ny]
        fish[a[nx][ny][0]], a[nx][ny] = [], []

        # 여기서 d는 상어의 방향
        dfs(nx, ny, temp2[1], cnt + temp2[0] + 1)

        # 복원 => 할때 nx, ny를 x, y로 바꾸기 => while문 안에서 원래 x,y의 방향 * 2만큼 간거 다시 순회
        a, fish = temp_a, temp_fish
        fish[a[nx][ny][0]], a[nx][ny] = temp1, temp2
        x, y = nx, ny

# 얘는 그냥 옮겨주면 된다
def move_fish(sx, sy):
    # 물고기는 번호 순대로 움직인다
    for i in range(16):
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            for _ in range(9):
                nx, ny = x + dx[a[x][y][1]], y + dy[a[x][y][1]]
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == sx and ny == sy):
                    a[x][y][1] = (a[x][y][1] + 1) % 8
                    continue
                if a[nx][ny]:
                    fish[a[nx][ny][0]] = [x, y]
                a[nx][ny], a[x][y] = a[x][y], a[nx][ny]
                fish[i] = [nx, ny]
                break


a = [[] for _ in range(4)]
fish = [[] for _ in range(16)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        a[i].append([temp[j]-1, temp[j+1]-1])
        fish[temp[j]-1] = [i, j // 2]

ans = 0
d, cnt = a[0][0][1], a[0][0][0] + 1
fish[a[0][0][0]], a[0][0] = [], []
# 상어는 0,0부터 먹어치우기 시작하므로 자연스러운 시작
dfs(0, 0, d, cnt)
print(ans)

'''
으아아아 좀더 집중해서 풀자!!!!


dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, -1, -1, -1, 0, 1, 1, 1)

sea = []
# 위치
fishes = [0] * 17

# sea = [
#   [[7,6], [2,3], [15,6], [9,8]],
#   [[3,1], [1,8], [14,7], [10,1]],
#   [[6,1], [13,6], [4,3], [11,4]],
#   [[16,1], [8,7], [5,2], [12,2]],
# ]

for i in range(4):
  line = list(map(int, input().split()))
  line_result = []
  for j in range(0, 8, 2):
    fishes[line[j]] = (i, j // 2)
    line_result.append([line[j], line[j+1]])
  sea.append(line_result)

score = sea[0][0][0]
fishes[sea[0][0][0]] = (-1,-1)

sea[0][0][0] = 0
shark = (0,0, sea[0][0][1])

print(fishes)
print(sea, '바다')

while True:
  #! 그리디하게 접근할 수 없었다. 그냥 DFS 돌려서 모든 경우를 보아야 했음 
  for i in range(1, 17):
    r,c = fishes[i]
    if (r > -1):
      d = sea[r][c][1] - 1
      count = 0
      while count < 8:
        nr = r + dr[d]
        nc = c + dc[d]
        if (-1 < nr < 4) and (-1 < nc < 4) and (sea[nr][nc][0] > 0):
          # 서로의 위치 바꾸기
          fishes[i], fishes[sea[nr][nc][0]] = fishes[sea[nr][nc][0]], fishes[i]
          # 바뀐 방향도 반영
          sea[r][c], sea[nr][nc] = sea[nr][nc], [sea[r][c][0], d]
          break
        else:
          count += 1
          d = (d + 1) % 8

  # 상어
  eat_fishes = []
  flag = False
  sr, sc, sd = shark
  for _ in range(4):
    nsr = sr + dr[sd]
    nsc = sc + dc[sd]
    if (-1 < nsr < 4) and (-1 < nsc < 4) and (sea[nsr][nsc][0] > 0):
      eat_fishes.append((*sea[nsr][nsc], nsr, nsc))
      sr, sc = nsr, nsc
      flag = True
    else:
      break

  # 뽑아서 먹기
  if flag:
    sr, sc, sd = shark
    # 힙써도 될듯
    eat_fishes.sort(reverse=True, key=lambda x:x[0])
    id, new_d, fr, fc = eat_fishes[0]
    score += id
    fishes[id] = (-1, -1)
    sea[sr][sc] = [-1, -1]
    sea[fr][fc] = [0, new_d]
    shark = (fr, fc, new_d)
  else:
    break
  print(sea)

print(score)

'''