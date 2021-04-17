def move(t, sr, sc):
  s_green = [sc]
  s_blue = [sr]

  if t == 2:
    s_green = [sc, sc+1]
  elif t == 3:
    s_blue = [sr, sr+1]

  gr = 5
  for gc in s_green:
    for r in range(6):
      if green[r][gc] != 0:
        gr = min(r-1, gr)
        break

  green[gr][sc] = 1

  if t == 2:
    green[gr][sc+1] = 1
  elif t == 3:
    green[gr-1][sc] = 1

  bc = 5
  for br in s_blue:
    for c in range(6):
      if blue[br][c] != 0:
        bc = min(c-1, bc)
        break

  blue[sr][bc] = 1
  if t == 2:
    blue[sr][bc-1] = 1
  elif t == 3:
    blue[sr+1][bc] = 1

def evaluate():
  global score, green, blue
  
  r = 5
  while r > -1:
    if sum(green[r]) == 4:
      green = [[0]*4] + green[:r] + green[r+1:]
      score += 1
    else:
      r -= 1

  if sum(green[0]) > 0:
    green = [[0]*4] + [[0]*4] + green[:4]
  elif sum(green[1]) > 0:
    green = [[0]*4] + green[:5]

  c = 5
  while c > -1:
    sum_c = 0

    for r in range(4):
      sum_c += blue[r][c] 

    if sum_c == 4:
      for i in range(4):
        blue[i] = [0] + blue[i][:c] + blue[i][c+1:]
      score += 1
    else:
      c -= 1

  sum_zero = 0
  sum_one = 0
  for r in range(4):
    sum_zero += blue[r][0] 
  for r in range(4):
    sum_one += blue[r][1] 

  if sum_zero > 0:
    for i in range(4):
      blue[i] = [0, 0] + blue[i][:4]
  elif sum_one > 0:
    for i in range(4):
      blue[i] = [0] + blue[i][:5]

N = int(input())

blue = [[0]*6 for _ in range(4)] 
green = [[0]*4 for _ in range(6)]

score = 0

for _ in range(N):
  t, r, c = map(int, input().split())
  move(t,r,c)
  evaluate()

sum1 = sum2 = 0
for g in green:
  sum1 += sum(g)
for b in blue:
  sum2 += sum(b)

print(score)
print(sum1 + sum2)