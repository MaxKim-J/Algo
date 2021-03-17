from collections import deque


#! 방향을 숫자로 나타내면 좀더 쉽게 방향전환을 구현할 수 있음
def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def start():
    direction = 1  # 초기 방향
    time = 1  # 시간
    y, x = 0, 0  # 초기 뱀 위치
    visited = deque([[y, x]])  # 방문 위치
    #! 최대한 생성한 자료구조를 그대로 이용하는 것이 좋다 => 이런 부분은 한번 생각해볼 것
    arr[y][x] = 2
    while True:
        #! 꼬리와 뱀을 가리키는 포인터를, 맨 끝에 2로 두면 나중에 자신의 몸을 만났을때를 좀더 쉽게 알 수 있음
        #! direction의 번호랑 연계해서 가야될 방향을 표현
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1:  # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                #! 그리고 이런식으로 맨 끝에 있는 방문 위치를 제거함으로서 더 쉽게 접근 가능 => 문제 그대로 구현하는 것
                arr[temp_y][temp_x] = 0  # 꼬리 제거
            arr[y][x] = 2
            #! 방문 위치는 계속 기록하는게 여러모로 유용
            visited.append([y, x])
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time


if __name__ == "__main__":

    # input
    N = int(input())
    K = int(input())
    arr = [[0] * N for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a - 1][b - 1] = 1  # 사과 저장
    L = int(input())
    times = {}
    for i in range(L):
        X, C = input().split()
        times[int(X)] = C
    print(start())



'''
N = int(input())
board = []
for _ in range(N+1):
  board.append([0] * (N+1))

K = int(input())
for _ in range(K):
  r, c = map(int, input().split())
  board[r][c] = -1

change = [0] * (N**2 + 1)
L = int(input())
for _ in range(L):
  x, way = input().split()
  change[int(x)] = way

def go_way(x, way):
  s1, s2 = x
  if way == 'right':
    return (s1, s2 + 1)
  elif way == 'left':
    return (s1, s2 - 1)
  elif way == 'up':
    return (s1 - 1, s2)
  elif way == 'down':
    return (s1 + 1, s2)

def change_way(current, direction):
  if direction == 'L':
    if current == 'right':
      return 'up'
    elif current == 'up':
      return 'left'
    elif current == 'down':
      return 'right'
    elif current == 'left':
      return 'down'
  elif direction == 'D':
    if current == 'right':
      return 'down'
    elif current == 'up':
      return 'right'
    elif current == 'down':
      return 'left'
    elif current == 'left':
      return 'up'

def solve():
  global board
  second = length = 1
  path = [(1,1)]
  way = 'right'

  for _ in range(N**2):
      second += 1
      s1, s2 = go_way(path[0], way)
      print(s1,s2)
      if (0 < s1 <= N) and (0 < s2 <= N):
        for i in range(1, length):
          p1,p2 = path[i]
          if p1 == s1 and p2 == s2:
            return second
        path.insert(0, (s1, s2))
        if board[s1][s2] == -1:
          board[s1][s2] = 0
          length += 1
        if change[second]:
          new_way = change_way(way, change[second])
          way = new_way
      else:
        return second

print(solve())
'''