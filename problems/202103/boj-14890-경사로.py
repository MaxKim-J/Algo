import sys
input = sys.stdin.readline

def check(li):
    # 경사로를 어디에다가 두었는지 기록
    sw = [False for i in range(n)]

    # 배열의 모든 요소를 끝빼고 다 순회
    for i in range(n - 1):

        # 높이가 계속 같은 곳은 평가할 필요 없음
        if li[i] == li[i + 1]:
            continue

        # 앞 뒤 차이가 2이상 난다면 그건 경사로를 놓더라도 지나갈 수 없는 길
        if abs(li[i] - li[i + 1]) > 1:
            return False

        # 차이가 1이 날 경우 경사로를 놓을 수 있음

        # 내려오는 경사로를 만들 수 있는 경우
        if li[i] > li[i + 1]:
            temp = li[i + 1]
            for j in range(i + 1, i + 1 + l): # 지점의 앞으로 l만큼 전진해서 경사로 설치 가능한지 체크
                if 0 <= j < n:
                    # 면적이 안되서 설치가 안되는 경우
                    if li[j] != temp: return False
                    # 이미 설치가 되어버린 경우
                    if sw[j] == True: return False
                    sw[j] = True
                else:
                    return False
        # 올라가는 경사로를 수 있는 경우 (li[i] < li[i + 1])
        else:
            temp = li[i]
            for j in range(i, i - l, -1): # 지점의 뒤로 l만큼 후진해서 경사로 설치 가능한지 체크
                if 0 <= j < n:
                    if li[j] != temp: return False
                    if sw[j] == True: return False
                    sw[j] = True
                else:
                    return False
    return True

n, l = map(int, input().split())
s = []

for i in range(n):
    s.append(list(map(int, input().split())))

cnt = 0

# 배열과 회전한 배열 모두 해주기
for i in s:
    if check(i):
        cnt += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(s[j][i])
    if check(temp):
        cnt += 1

print(cnt)

'''
조건을 다 추리기가 너무 어려웠음ㅜㅜ

turn_board = []

for i in range(n):
  turn_board.append(list(map(lambda x:x[i], board)))


def put_hill(temp, pos):
  temp_prev = temp[pos]
  for n in range(l):
    temp[pos+n] += 1

  for m in range(pos-1, -1, -1):
    if temp[m] == temp_prev:
      temp[m] += 1
    else:
      break

def row_evaluate(row):
  temp = row[:]
  prev = row[0]
  repeat = 1

  for i in range(1, n):
    if row[i] < prev:
      return False

    if prev == row[i]:
      repeat += 1

    if (repeat >= l) and (row[i] == prev + 1):
      put_hill(temp, i - l)
      if (row[i] == temp[i-1]):
        repeat += 1
      else:
        repeat = 1

    prev = row[i]

  print(row, temp)

  for t in temp:
    if t != temp[0]:
      return False
  return True

def board_evalute(board):
  global count
  for row in board:
    row_reverse = list(reversed(row))
    a = row_evaluate(row)
    b = row_evaluate(row_reverse)
    if a or b:
      print(row)
      count += 1

count = 0

board_evalute(board)
board_evalute(turn_board)

print(count)

# print(row_evaluate([1, 1, 2, 3, 3, 3]))
'''