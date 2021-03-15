'''
너무 무식하게 푸려다가 한시간안에 못품...
조건을 진짜 잘 나눠줘야 하는 문제였다
전체적인 접근과 방향은 맞았다고 할 수 있지만 역시 구현이 어려웠음
4차원 배열...지린다...

코드를 그냥 손으로 막 쓰는게 별로 의미가 없는것 같다. 시간만 낭비임
핵심 아이디어들을 나열하고 거기서 스켈레톤을 뽑아내는게 더 나은듯
'''


N, M = map(int, input().split())
B = [list(input().rstrip()) for _ in range(N)]  # Board
dx = [-1, 1, 0, 0]  # x축 움직임
dy = [0, 0, -1, 1]  # y축 움직임
queue = []  # BFS : queue 활용

# Red(rx,ry)와 Blue(bx,by)의 탐사 여부 체크
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0  # 초기화
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx, ry = i, j
            elif B[i][j] == 'B':
                bx, by = i, j
    # 위치 정보와 depth(breadth 끝나면 +1)
    queue.append((rx, ry, bx, by, 1))

    #* depth를 저장해줄 필요는 없었다 => 방문한 노드의 하위 트리는 몇번을 해도 반복되는 연산임
    visited[rx][ry][bx][by] = True

#! 한번에 계속 이동한다 => 판을 굴리면 구슬이 한 방향으로 계속 굴러간다(?????? - 이걸 몰랐네..)
def move(x, y, dx, dy):
    cnt = 0  # 이동 칸 수
    # 다음이 벽이거나 현재가 구멍일 때까지
    #! 해당 방향으로 일보전진 하지 못하는 경우는 이렇게 딱 2가지
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solve():
    pos_init()  # 시작 조건
    while queue:  # BFS : queue 기준
        rx, ry, bx, by, depth = queue.pop(0)
        if depth > 10:  # 실패 조건
            break
        for i in range(4):  # 4방향 이동 시도
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # Red
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  # Blue

            #! 어찌되었든 파랑이 밖으로 나오면 무조건 실패
            if B[nbx][nby] != 'O':  # 실패 조건이 아니면
                if B[nrx][nry] == 'O':  # 성공 조건
                    print(depth)
                    return

                #* 이거 뭐야;;;;; ㅁㅊ다;;; 이동거리가 많은 것이 원래 방향에서 뒤에 있었을 것이기 때문에
                if nrx == nbx and nry == nby:  # 겹쳤을 때
                    if rcnt > bcnt:  # 이동거리가 많은 것을
                        nrx -= dx[i]  # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                # breadth 탐색 후, 탐사 여부 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    # 다음 depth의 breadth 탐색 위한 queue
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)  # 실패 시

solve()