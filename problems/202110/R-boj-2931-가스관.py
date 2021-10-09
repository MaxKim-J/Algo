from collections import deque
import sys

'''
못품
아 너무 어렵다;;

Z와 D를 기준으로 모두 BFS를 시작해서, 뚫려있는 부분을 구한다음에 정확하게 어디를 막아야 할지 도출해야한다
생각을 깊게 많이 해봤어야 풀 수 있는 문제였다... 역시 명징한 해가 나올때까지 경거망동 코딩을 하면 안된다 무조건 망함
시간을 맞추는거랑 명징한 해를 구하는 연습을 계속해서 해 나가야겠다.
방향을 모두 통합해서 구하는 것도 좋은 방식인듯 하다
'''

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def direction(s): # 새로운 블럭에서 진입 가능한 방향을 리턴한다
    if s == '|':
        return [1, 3]
    elif s == '-':
        return [0, 2]
    elif s == '+' or s == 'M' or s == 'Z':
        return [0, 1, 2, 3]
    elif s == '1':
        return [0, 1]
    elif s == '2':
        return [0, 3]
    elif s == '3':
        return [2, 3]
    elif s == '4':
        return [1, 2]

def bfs(x, y, dir):
    global fx, fy
    q = deque()
    q.append([x, y, dir])
    c[x][y] = 1
    while q:
        x, y, dir = q.popleft()
        for d in dir:
            nx = x + dx[d] # 그 칸에서 나갈 수 잇는 방향만 평가한다
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n and not c[nx][ny]:
                # 방향대로 갔을 때 . 을 만나기 전까지는 계속 방향대로만 간다
                if a[nx][ny] != '.':
                    c[nx][ny] = 1
                    ndir = direction(a[nx][ny]) # 새로운 블럭으로 진입이 가능한 방향들 리턴 = 이게 나중에 그 칸에서 나갈 수 있는 방향
                    q.append([nx, ny, ndir])
                else:
                    # .을 처음으로 만나면 그 포인트가 뚫려있다는 것이다
                    if a[x][y] == 'M' or a[x][y] == 'Z':
                        continue

                    # 뚫려있는 그 포인트를 저장하게 된다
                    # 얘는 Z에서 오든 M에서 오든 이 지점은 똑같다
                    if not fx and not fy:
                        fx, fy = nx + 1, ny + 1

                    nd = (d+2) % 4 # 반대로 돌리기
                    # 온 방향과 반대방향으로 진입해야 한다
                    # 0번으로 진입해서 .을 발견했다면 걔는 2가 뚫려있어야 한다

                    if nd not in check_list:
                        check_list.append(nd)

m, n = map(int, input().split())
c = [[0] * n for _ in range(m)]

a = []
for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j in range(n):
        if row[j] == 'M':
            sx, sy = i, j
        elif row[j] == 'Z':
            zx, zy = i, j

check_list, fx, fy = [], 0, 0
bfs(sx, sy, [0, 1, 2, 3])
bfs(zx, zy, [0, 1, 2, 3])

for i in range(m):
    for j in range(n):
        if a[i][j] != '.' and not c[i][j]:
            bfs(i, j, direction(a[i][j]))

# M에서 오든 Z에서 오든 뚫려있는 한 좌표의 방향을 설정
check_list.sort()

if len(check_list) == 4:
    print(fx, fy, '+')
else:
    block_list = ['|', '-', '1', '2', '3', '4']
    for s in block_list:
        if check_list == direction(s):
            print(fx, fy, s)