'''
주사위 하나를 고정된 배열로 놓고, 숫자를 바꾸는게 훨씬 용이한 접근이었다
내 방법은 디버깅이 너무 힘들었음ㅜㅜ
문제에 충실하게, 자연스럽게, 문제의 힌트를 죄다 이용하며 푸는 방법이 뭔지 생각해봐야한다
'''

# 맨위는 arr[1], 맨 아래는 arr[6] => 그림으로 나온 눈금을 위치값으로 사용하면 되었다
def move(n, arr):
    if n == 1:    # 동
        return [0, arr[3], arr[2], arr[6], arr[1], arr[5], arr[4]]
    elif n == 2:  # 서
        return [0, arr[4], arr[2], arr[1], arr[6], arr[5], arr[3]]
    elif n == 3:  # 북
        return [0, arr[2], arr[6], arr[3], arr[4], arr[1], arr[5]]
    elif n == 4:  # 남
        return [0, arr[5], arr[1], arr[3], arr[4], arr[6], arr[2]]


if __name__ == "__main__":

    # input
    N, M, y, x, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    order = list(map(int, input().split()))

    dice = [0] * 7  # 주사위

    dy = [0, 0, 0, -1, 1]
    dx = [0, 1, -1, 0, 0]

    # 명령 수행
    for i in range(len(order)):
        if y + dy[order[i]] < 0 or y + dy[order[i]] >= N or x + dx[order[i]] < 0 or x + dx[order[i]] >= M:
            continue
        else:
            x, y = x + dx[order[i]], y + dy[order[i]]  # 좌표 이동
            dice = move(order[i], dice)  # 주사위 이동

            if arr[y][x] == 0:
                arr[y][x] = dice[6]  # 주사위 -> 칸
            else:
                dice[6] = arr[y][x]  # 칸 -> 주사위
                arr[y][x] = 0  # 칸에 있는 수 0으로 수정

            print(dice[1])
            
'''
N, M, X, Y, K = map(int, input().split())
board = []

for _ in range(N):
  board.append(list(map(int, input().split())))

orders = list(map(lambda x:x-1, map(int, input().split())))

dice = [0,0,0,0,0,0]
way = [[2,5,1,4], [2,5,3,0], [4,1,3,0], [2,5,4,1], [2,5,0,3], [1,4,3,0]]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def get_apposite(top):
  if top < 3:
    return top + 3
  elif top >= 3:
    return top - 3

current = (X, Y)
top = 1

for order in orders:
  r, c = current
  bottom = get_apposite(top)

  if board[r][c] == 0:
    board[r][c] = dice[bottom]
  else:
    dice[bottom] = board[r][c]
    board[r][c] = 0
  print(board, dice)

  nr = r + dr[order]
  nc = c + dc[order]

  if (-1 < nr < N) and (-1 < nc < M):
    current = (nr, nc)
    bottom = way[top][order]
    print(dice[get_apposite(bottom)])
'''
    
