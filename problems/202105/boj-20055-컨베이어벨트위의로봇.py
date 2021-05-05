N, K = map(int, input().split())

'''
deque.rotate라는 내장 함수가 있는데 훨씬 빠르다(2배 빠름)
배열을 굳이 이차원이 아니라 1차원 배열만 쓰고 그거 deque로 rotate하는 것이 젤 빨랐음
1차원으로 하는게 확실히 나을거같긴 하다
'''

belt_input = list(map(int, input().split()))
belt = [belt_input[:N], list(reversed(belt_input[N:]))]
robots = [0] * N

def move_belt():
  global robots, belt
  new_belt = [[0] * N for _ in range(2)]
  for r in range(2):
    for c in range(N):
      if r == 0:
        if c == N-1: # 내리는 자리
          new_belt[1][c] = belt[r][c]
        else:
          new_belt[r][c+1] = belt[r][c]
      else:
        if c == 0: # 올리는 자리
          new_belt[0][c] = belt[r][c]
        else:
          new_belt[r][c-1] = belt[r][c]
  belt = new_belt
  robots = [0] + robots[:-1]
  robots[-1] = 0

# 2,3
def move_robot():
  global robots, belt
  for i in range(N-2, -1, -1):
    if (robots[i] == 1) and (robots[i+1] == 0) and (belt[0][i+1] >= 1):
      robots[i], robots[i+1] = robots[i+1], robots[i]
      belt[0][i+1] -= 1

  if belt[0][0] > 0 and robots[0] == 0:
    robots[0] = 1
    belt[0][0] -= 1

count = 1

while True:
  move_belt()
  move_robot()
  malformed = 0
  for i in range(2):
    malformed += belt[i].count(0)
  if malformed >= K:
    print(count)
    break
  count += 1
  

