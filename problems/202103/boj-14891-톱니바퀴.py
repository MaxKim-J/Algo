gears = []

for _ in range(4):
  gears.append(list(input()))

k = int(input())

def calculate(relation, direction):
  if relation:
    return 0
  else:
    if direction == 1:
      return -1
    elif direction == -1:
      return 1
    else:
      return 0

def get_rotate_directions(gear, direction):
  r01 = gears[0][2] == gears[1][6]
  r12 = gears[1][2] == gears[2][6]
  r23 = gears[2][2] == gears[3][6]

  result = [0,0,0,0]

  if gear == 0:
    result[0] = direction
    result[1] = calculate(r01, result[0])
    result[2] = calculate(r12, result[1])
    result[3] = calculate(r23, result[2])
  elif gear == 1:
    result[1] = direction
    result[0] = calculate(r01, direction)
    result[2] = calculate(r12, direction)
    result[3] = calculate(r23, result[2])
  elif gear == 2:
    result[2] = direction
    result[3] = calculate(r23, direction)
    result[1] = calculate(r12, direction)
    result[0] = calculate(r01, result[1])
  elif gear == 3:
    result[3] = direction
    result[2] = calculate(r23, result[3])
    result[1] = calculate(r12, result[2])
    result[0] = calculate(r01, result[1])
  return result

def rotate(directions):
  global gears
  for i in range(4):
    direct = directions[i]
    gear = gears[i][:]

    if direct == 1:
      gear =  [gear[-1]] + gear[:-1]
    elif direct == -1:
      gear = gear[1:] + [gear[0]]
      
    gears[i] = gear

for _ in range(k):
  gear, direction = map(int, input().split())
  rotate(get_rotate_directions(gear - 1, direction))

score = 0
for i in range(4):
  if gears[i][0] == '1':
    score += (2 ** i)

print(score)
