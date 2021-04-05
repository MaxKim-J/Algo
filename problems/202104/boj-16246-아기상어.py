# ㄹㅇ 개 야매풀이 ㅋㅋㅋ 재밌어서 가져와봄
# BFS로 상어가 갈 수 있는 모든 경우의 수를 탐색해야 했기 때문에 굳이 일일히 구현할 필요는 없는 문제였음

from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, weight, time, eat):
    q, can_eat = deque(), []
    q.append([x, y])
    c = [[-1]*n for _ in range(n)]

    # depth를 새로운 visited의 시작 위치(상어 위치)에 끼우고, visited도 초기화해서 시작
    c[x][y] = time

    while q:
      # 최초의 qlen은 1, 탐색하려는 노드가 queue에 들어오면 큐의 개수만큼 인접한 노드들에 depth를 기록
      # 되게 야매풀이인듯..? 이거 좀 정석으로 대체할 수 있는 방법이 있을거같은데 잘 모르겟다
      qlen = len(q)
      while qlen:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이거슨 비슷한 접근이긴 했네..
            if 0 <= nx < n and 0 <= ny < n:
                # 방문하지 않은 칸일 경우 방문
                if c[nx][ny] == -1:
                    if a[nx][ny] == 0 or a[nx][ny] == weight:
                        # visited에는 거리를 기록함 => 이거 depth가 됨(한번에 한칸씩만 가므로)
                        # 재귀를 거듭하면서 새로운 depth가 새로운 visited에 계속 기록됨
                        c[nx][ny] = c[x][y] + 1
                        q.append([nx, ny])
                    elif 0 < a[nx][ny] < weight: # 먹을 수 있는 물고기를 죄다 배열에 저장
                        can_eat.append([nx, ny])
        qlen -= 1

      # 먹을 수 있는 물고기가 있는지 없는지를 계속 감시
      if can_eat:
          # 배열에 저장한 것 중 가장 최솟값의 물고기를 먹음(가장 왼쪽, 가장 위 물고기) - 음 이생각은 못해따;;
          nx, ny = min(can_eat)
          eat += 1
          if eat == weight:
              eat = 0
              weight += 1
          # 먹은 물고기는 없앰
          a[nx][ny] = 0
          # 희한한게 거리를? 리턴함
          return nx, ny, weight, c[x][y] + 1, eat

    print(time)
    sys.exit()

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            # 상어의 위치를 기록하고 그냥 0부터 시작함(depth를 기록하려는 것)
            a[i][j] = 0

weight, time, eat = 2, 0, 0

# 해괴한 스킬....재귀로 반복시킴
while True:
    x, y, weight, time, eat = bfs(x, y, weight, time, eat)