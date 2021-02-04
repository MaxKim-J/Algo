import sys
from collections import deque

#! 쌉고수풀이
# 섬마다 번호 붙이기
# id를 음수값으로 붙여서 처음의 데이터와 구분
# 순회하다가 맨 처음 만난 1부터 -1섬이 됨


def grouping(i, j):
    q = deque([(i, j)])
    world[i][j] = gid  # * gid를 넣어줌
    while q:
        qi, qj = q.popleft()
        for t in range(4):
            x, y = qi + dx[t], qj + dy[t]
            if 0 <= x < n and 0 <= y < n:
                # 육지인 경우 순회
                if world[x][y] == 1:
                    world[x][y] = gid
                    q.append((x, y))
                # 바다인 경우 따로 모아다가 큐에 넣어줌 => 여기서는 육지와 바다가 접한 바닷가가 됨
                #! 그럼 순회하는 순서가 -1섬의 바닷가부턴가
                elif world[x][y] == 0 and not (qi, qj) in ocean:
                    ocean.append((qi, qj))

 #! Ocean에 넣은 순서대로라면 -1 섬부터 간척사업을 하는데 바닷가를 한번씩 일단 순회한후
 #! 자동으로 다음 섬으로 넘어가게 된다
 #! 그리고 그렇게 한번씩 상하좌우칸 간척사업하면 다시 -1섬 간척할때 append한 얘들 다시 순회
 #! 오우....이거 큐에 대해서 잘 이해하고 있어야 이렇게 풀 수 있는 거였네

# 고로 얘는 모든 섬에서 동시에 확장하는 꼴이 된다 => 다만 순서대로


def get_distance():
    loop = 0
    ans = sys.maxsize
    # 바닷가부터 순회 시작!
    while ocean:
        # 거리를 구해주기 위해 몇번의 간척이 일어나는지 새준다(loop 변수)
        loop += 1
        length = len(ocean)
        for _ in range(length):
            oi, oj = ocean.popleft()
            for t in range(4):
                x, y = oi + dx[t], oj + dy[t]
                #! 여기가 핵심이네 - world에는 이미 섬 구분이 되있는 상황
                if 0 <= x < n and 0 <= y < n:
                    # * 아직 육지가 안된 바다일 경우 => 육지로 만들고 계속 순회
                    if world[x][y] == 0:
                        world[x][y] = world[oi][oj]
                        ocean.append((x, y))
                    # * 여기는 간척이된 육지와 육지가 만났을 때 => 일단 기본적으로 loop * 2

                    # ? 이동하려는 좌표의 그룹번호가 현재 그룹보다 낮은 경우
                    #! 이미 저번 loop에서 이어져있는데 이제 안 것 => loop에서 하나를 뺀다
                    elif world[x][y] < world[oi][oj]:
                        ans = min(ans, (loop - 1) * 2)

                    # ? 이동하려는 좌표의 그룹번호가 현재 그룹보다 높은 경우
                    #! 같은 루프에서 중복된 곳에 간척을 하려고 했기 때문에 전체에서 1을 뺀다
                    elif world[x][y] > world[oi][oj]:
                        ans = min(ans, loop * 2 - 1)
    return ans


dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
n = int(sys.stdin.readline())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ocean = deque()
gid = -1

# 섬을 그룹으로 짝지어줌
for i in range(n):
    for j in range(n):
        if world[i][j] > 0:
            grouping(i, j)
            gid -= 1
sys.stdout.write(str(get_distance()))

# 토마토 문제도 풀어봐야겠다
