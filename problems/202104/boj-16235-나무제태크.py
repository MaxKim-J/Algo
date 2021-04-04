# 조건이 복잡한 구현문제..

dr = (0, 0, 1, -1, 1, -1, 1, -1)
dc = (1, -1, 0, 0, 1, -1, -1, 1)

N, M, K = map(int, input().split())
A = []

for _ in range(N):
  A.append(list(map(int, input().split())))


land = [[[] for _ in range(N)] for _ in range(N)]
nutrition = [[5]*N for _ in range(N)]

for _ in range(M):
  r, c, age = map(int, input().split())
  land[r-1][c-1].append(age)

def spring():
  for r in range(N):
    for c in range(N):
      trees = sorted(land[r][c])
      for i in range(len(trees)):
        if nutrition[r][c] < trees[i]:
          trees[i] = -(trees[i])
        else:
          nutrition[r][c] -= trees[i]
          trees[i] += 1
      land[r][c] = trees

def summer():
  for r in range(N):
    for c in range(N):
      trees = land[r][c]
      new_trees = []
      for i in range(len(trees)):
        if trees[i] < 0:
          nutrition[r][c] += ((-trees[i]) // 2)
        else:
          new_trees.append(trees[i])
      land[r][c] = new_trees

def autumn():
  for r in range(N):
    for c in range(N):
      trees = land[r][c]
      for i in range(len(trees)):
        if trees[i] % 5 == 0:
          for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1 < nr < N and -1 < nc < N:
              land[nr][nc].append(1)

def winter():
  for r in range(N):
    for c in range(N):
      nutrition[r][c] += A[r][c]

for _ in range(K):
  spring()
  summer()
  autumn()
  winter()

result = 0

for r in range(N):
  for c in range(N):
    result += len(land[r][c])

print(result)