# 일단 이거는 ㄹㅇ 개 야매풀이 ㅋㅋㅋ 재밌어서 가져와봄

#! 핵심 : 따로 기록하기, 왼쪽 위쪽이 뭔지, 과정을 다 구현할 필요가 없음

# BFS로 상어가 갈 수 있는 모든 경우의 수를 탐색해야 했기 때문에 굳이 일일히 구현할 필요는 없는 문제였음
# 정석적으로 BFS에 모든 상황 이차원 배열을 넣어서 풀수도 있었을 거 같긴 한데
# 상어랑 같은 크기의 물고기가 있을때 어떻게 기록할 것인지 + 가장 왼쪽 위의 물고기를 어캐 픽할것인지 => 생각해봐야햇음
# board에다가 직접 기록하지말고, 상어의 위치와 상어가 빠졌지만 변화가 수정된 board를 죄다 큐에 밀어넣는 방식이면 될지도(물론 메모리가)
#! BFS를 할때도 어떻게 자료구조 짜는게 좋은지 생각을 잘해봐야됨 큐에 뭐까지 넣을지, 기록은 어떻게 해야할지
# r, c, depth, board => 이렇게 넣었으면 가능했으려나...

from collections import deque
import sys

input = sys.stdin.readline
# 이거는 이제 별 상관이 없어졌음
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
      # 되게 야매풀이인듯..? queue에 이차원 배열을 넣어주면 좀 정석으로 풀 수 있을것은 같음
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

      #! 먹을 수 있는 물고기가 있는지 없는지를 정리
      if can_eat:
          # 배열에 저장한 것 중 가장 최솟값의 물고기를 먹음(가장 왼쪽, 가장 위 물고기) - 음 이생각은 못해따;;
          # 해당 depth에서 탐색할 수 있는 모든 자리에서 먹을 수 있는 물고기중에 가장 왼쪽 위 물고기를 먹는거임
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

'''
정석에 가까운 풀이

import sys
from collections import deque
import heapq

# 먹는 물고기 리턴하는 함수 => 한번 할때마다 먹을 수 있는(reach가 가능한) 물고기를 일단 다 배열에 넣는 느낌이다
# arr를 modify하지 않음 걍 탐색만함 갈수 있는 곳으로만 간다
def bfs(x, y):
    q = deque()
    heap = []
    q.append((x, y, 0))

    while q:
        x, y, d = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == 0 or size == arr[nx][ny]:
                    q.append((nx, ny, d + 1))
                elif size > arr[nx][ny]:
                    # 힙을 사용해서 왼쪽위쪽이 가장 앞에 오게 만들기
                    # 큐에는 뎁쓰랑 새로운 노드 좌표가 들어감 => 뎁쓰 어따씀???
                    heapq.heappush(heap, [d + 1, nx, ny])

    # 먹는 물고기를 리턴
    if heap:
        return heap[0]
    else:
        return None


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline
n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

# 초기화
fishes = []
size = 2 # 상어의 사이즈는 또 따로 기록해주기
eaten = 0 # 먹었던것들 기록(상어 레벨업때문에)
cnt = 0 # 답(depth, time)

s1, s2 = 0, 0 # 최초의 상어위치 기록

for i in range(n):
    for j in range(n):
        # 물고기 기록
        if 0 < arr[i][j] < 7:
            fishes.append((i, j))
        # 상어 기록. 이때 보드의 상어 자리를 0으로 만들고 자리를 기록
        elif arr[i][j] == 9:
            arr[i][j] = 0
            s1 = i
            s2 = j

# 물고기 기록한것에서 그 물고기들 다 먹었는지 체크
#! 실제로는 하나만 먹으면 되고 거기로만 가면 됨 굳이 모든 과정 다 거쳐서 거까지 갈 필요가 없음

while len(fishes) != 0:
    # 매번 BFS 수행할때마다 visited 초기화
    visited = [[False] * n for _ in range(n)]
    visited[s1][s2] = True

    result = bfs(s1, s2)

    # 먹을 수 있는 물고기가 있는지 타진 없으면 브레이크
    if result == None:
        break
    else:
        eaten += 1
        cnt += result[0]
        arr[result[1]][result[2]] = 0

    if eaten == size:
        eaten = 0
        size += 1

    # 먹은 물고기 자리
    s1, s2 = result[1], result[2]

print(cnt)
'''