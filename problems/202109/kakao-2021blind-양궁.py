from collections import deque

n = int(input())
info=list(map(int, input().split()))

answer=[]

def get_score(string):
  apeach = 0
  lion = 0
  arr = list(map(int, list(string)))
  for i in range(11):
    if info[i] >= arr[i]:
      if (arr[i] == 0) and (info[i] == 0):
        continue
      apeach += (10 - i)
    elif arr[i] > info[i]:
      lion += (10 - i)

  return (lion > apeach, lion-apeach)

def dfs():
  queue = deque([(n, '')])

  while queue:
    left, string = queue.pop()
    length = len(string)

    if left == 0:
      new_string = string + '0' * (11 - len(string))
      is_win, score = get_score(new_string)
      if is_win:
        answer.append((score, new_string))

    if length < 11:
      for j in range(left+1):
        new_string = string + str(j)
        queue.append((left-j, new_string))

dfs()

answer = sorted(answer, key=lambda x:(-x[0], x[1]))

if len(answer) == 0:
  print([-1])
else:
  print(list(map(int, answer[0][1])))