'''
- 함수없이 푸는 것도 나쁘진 않은듯
- 격자 0,1 인덱스 처음부터 잘 구분하자...
- 일의 순서를 생각하고 확실한 로직의 위치를 설정하자. 두루뭉술하게 넘기지 말것
- 문제 푸는데 사용하는 자료형을 적절히 분할하는 지혜...
- 자료형 전체를 죄다순회 하는 것을 피해야 함
'''

dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

N, M, k = map(int, input().split())
smells = [list(map(int, input().split())) for _ in range(N)]

sharks = []
sharks_pos = []

start_dir = list(map(int, input().split()))

for i in range(N):
  for j in range(N):
    if smells[i][j] > 0:
      sharks.append((smells[i][j], start_dir[smells[i][j] - 1] - 1))
      sharks_pos.append((i, j))
      smells[i][j] = [smells[i][j], k]

p = []
for i in range(M):
  tmp = []
  for _ in range(4):
    tmp.append(list(map(int, input().split())))
  p.append(tmp)

count = 0
while True:
  count += 1
  if count > 1000:
    print(-1)
    break

  go_shark = dict()
  for i in range(len(sharks)):
    id, dir = sharks[i]
    r, c = sharks_pos[i]
    goto1 = []
    goto2 = []
    for d in p[id-1][dir]:
      nr = r + dr[d]
      nc = c + dc[d]
      if (-1 < nr < N) and (-1 < nc < N):
        if smells[nr][nc] == 0:
          goto1.append(((nr, nc), d-1))
        elif smells[nr][nc][0] == id:
          goto2.append(((nr, nc), d-1))

    goto = goto1[0][0] if len(goto1) else goto2[0][0]
    new_d = goto1[0][1] if len(goto1) else goto2[0][1]
    if go_shark.get(goto):
      go_shark[goto].append((id, new_d))
    else:
      go_shark[goto] = [(id, new_d)]
  
  new_sharks = []
  new_sharks_pos = []
  for pos in go_shark.keys():
    if len(go_shark[pos]) == 1:
      id, new_dir = go_shark[pos][0]
    elif len(go_shark[pos]) > 1:
      id, new_dir = sorted(go_shark[pos], key=lambda x:x[0])[0]
    new_sharks.append((id, new_dir))
    new_sharks_pos.append(pos)
    smells[pos[0]][pos[1]] = [id, k]
  
  for r in range(N):
    for c in range(N):
      # 1초가 남았다면 0으로 만들어주기
      # 상어가 방금 갔던 자리 제외
      if (smells[r][c] != 0) and ((r,c) not in new_sharks_pos):
        if smells[r][c][1] == 1:
          smells[r][c] = 0
        else:
          smells[r][c][1] -= 1

  if len(new_sharks) == 1:
    print(count)
    break

  sharks = new_sharks[:]
  sharks_pos = new_sharks_pos[:]

'''
3배 빨랐던 풀이

import sys
input = sys.stdin.readline

# 기본적인 접근 틀은 비슷한데(빈도를 따지기 위해 딕셔너리 쓴다던가), 조금더 재귀스럽게 풀었음
# 변수를 아끼지 않았음
# move접근 

def move(alive, direc_shark, rc_shark, info_rc, time):
    #! 상어가 이미 있는지 여부를 집합으로 구분함
    occupied = set()
    next_alive = [0]*(M+1)
    next_direc_shark = [0]*(M+1)
    next_rc_shark = [(0, 0)]*(M+1)

    # 딕셔너리 복사
    next_info_rc = dict()
    for b, c in info_rc.items():
        next_info_rc[b] = c

    # 상어 죄다 순회하기
    for num in range(1, M+1):
        if not alive[num]:
            continue  # 이번 턴은 alive를 봐야해
        r, c = rc_shark[num]
        cur_direc = direc_shark[num]

        # 0 찾기
        flag = False
        for direc in priority_direc[num][cur_direc]:
            nr, nc = r+dr[direc], c+dc[direc]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            #!!!! 존나핵심
            #!!!! smells 배열의 시간을 맨날 줄여주거나 하지 않고, 그냥 한번 기록해놓은 후
            #!!!! time을 이용해서 시간이 만료되는지 보았음 => 이것때문에 시간 많이걸린듯
            #* 최대한 전체 자료형을 한번에 주무르지 않는 방법을 고를 필요가 있음 => 시간적인 리스크가 큼

            #! 이걸로 냄새 없는 칸 찾을 수 있음
            if info_rc[(nr, nc)][1] < time:
                flag = True #* 하나라도 0이 있었던 경우

                #! 이미 상어가 있다면 아예 그냥 기록하지 않음 => 상어는 냄새 딕셔너리 상으로는 0으로 기록
                if (nr, nc) in occupied:
                    break

                next_alive[num] = 1
                occupied.add((nr, nc))

                #! 기록을 해줄때 time+K로 기록해서, time이 늘어날때마다 없어지는 냄새를 구분할 수 있었음
                #* 이러면 루프를 돌때마다 상어가 직접 간 곳의 냄새만 바꿔주면 됨
                next_info_rc[(nr, nc)] = (num, time+K)
                next_direc_shark[num] = direc
                next_rc_shark[num] = (nr, nc)
                break

        # 0이 없으면 자신이 냄새를 뿌렸던 칸으로(상어 말고)
        if not flag:
            for direc in priority_direc[num][cur_direc]:
                nr, nc = r+dr[direc], c+dc[direc]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if info_rc[(nr, nc)][0] == num:
                    next_alive[num] = 1
                    occupied.add((nr, nc))
                    next_info_rc[(nr, nc)] = (num, time+K)
                    next_direc_shark[num] = direc
                    next_rc_shark[num] = (nr, nc)
                    break
    # 종료
    if sum(next_alive) == 1:
        return False
    return (next_alive, next_direc_shark, next_rc_shark, next_info_rc)


# 상하 좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M, K = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
direc_shark = [0] + list(map(lambda x: int(x)-1, input().split()))
priority_direc = [[]]
for num in range(M):
    priority_direc.append(
        # 이런거 그냥 입력 받을때부터 해주자... 괜히 뒤에서 헷갈림
        [list(map(lambda x:int(x)-1, input().split())) for _ in range(4)])

info_rc = dict()
alive = [0] + [1]*M
rc_shark = [(0, 0)]*(M+1)

#! 딕셔너리를 이용해서 배열의 정보를 모조리 저장
for r in range(N):
    for c in range(N):
        num = sea[r][c]
        if num:
            rc_shark[num] = (r, c)
            # 상어번호, 없어지는 시간(다녀간 시간 + K)
            info_rc[(r, c)] = (num, K)
        else:
            info_rc[(r, c)] = (0, 0)
time = 0

# 기본적으로는 재귀인데, 중간에 조건을 한번 확인하고 맞으면 계속 재귀해줌
while time < 1001:
    time += 1
    res = move(alive, direc_shark, rc_shark, info_rc, time)
    if not res:
        break
    alive, direc_shark, rc_shark, info_rc = res

if time > 1000:
    print(-1)
else:
    print(time)

'''





  