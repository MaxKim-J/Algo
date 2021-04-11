'''
1. 큰 배열을 직접 옮겨서 써야하는 상황에서;;; 오타를 내버림ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 아백준진짜..
2. 처음에는 시간초과였음 BFS내에서 모든 배열을 다 순회하면서 0이 없어졌는지 확인했기 때문
3. 입력받을때 0의 개수를 세주고 0을 그만큼 지웠는지 평가하는 것으로 시간 많이 줄임
4. 아 이건 return으로 하는게 더 편하겠군 싶은 생각이 들면 바로 함수로 분리하는게 나음. 그것도 스킬인듯
'''

from itertools import combinations
from copy import deepcopy

dr = (0,0,1,-1)
dc = (1,-1,0,0)

N, M = map(int, input().split())
board = []

for _ in range(N):
  board.append(input().split())

def BFS(queue, board, zero_count):
  time = 0
  count = zero_count
  while queue:
    if count == 0:
      return time
    new_queue = []
    time += 1
    for r,c in queue:
      for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (-1 < nr < N) and (-1 < nc < N):
           if (board[nr][nc] == '0') or (board[nr][nc] == '2'):
             if board[nr][nc] == '0':
               count -= 1
             board[nr][nc] = '*'
             new_queue.append((nr, nc))
    queue = new_queue[:]
  return 100000


possible = []
zero_count = 0

for r in range(N):
  for c in range(N):
    if board[r][c] == '2':
      possible.append((r, c))
    elif board[r][c] == '0':
      zero_count += 1


min_time = 100000

for virus in combinations(possible, M):
  c_board = deepcopy(board)
  queue = []
  for r, c in virus:
    c_board[r][c] = '*'
    queue.append((r,c))
  min_time = min(BFS(queue, c_board, zero_count), min_time)
  
print(-1 if min_time == 100000 else min_time)


  



