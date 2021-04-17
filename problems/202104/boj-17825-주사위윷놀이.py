dice = list(map(int, input().split()))

# dice = [5,1,2,3,4,5,5,3,2,4]
# dice = [1,1,1,1,1,1,1,1,1,1]
# dice = [5,5,5,5,5,5,5,5,5,5]
# dice = [1,2,3,4,1,2,3,4,1,2]

route = {
  5 : [10,13,16,19,25,30,35,40],
  10 : [20,22,24,25,30,35,40],
  15 : [30,28,27,26,25,30,35,40],
}

chess = [(0, 0), (0, 0), (0, 0), (0, 0)]

# chess를 꼭 DFS에서 같이 내려보낼 필요가 없었다. 
def DFS(score, depth):
  global result, chess

  if depth == 10:
    result = max(result, score)
    return

  for i in range(4):
    r, p = chess[i]

    if (r == -1) and (p == -1):
      continue

    new_score = score
    tmp = chess[:]
    
    nr = r
    np = p + dice[depth]

    if (nr == 0 and np > 19) or (nr > 0 and np > len(route[nr]) - 1):
      nr = np = -1
      new_chess = chess[:i] + [(nr, np)] + chess[i+1:]

    if (nr == 0) and (np in [5, 10, 15]):
      nr = np
      np = 0

    if (nr, np) not in chess:
      if (nr != -1) and (np != -1):
        new_chess = chess[:i] + [(nr, np)] + chess[i+1:]
        new_score += (np * 2) if (nr == 0) else route[nr][np]
    else:
      continue

    chess = new_chess
    DFS(new_score, depth + 1)
    chess = tmp

result = -1

DFS(0, 0)

print(result)

'''
주사위 수를 하나씩 빼가는 방법으로 풀이

import sys

input = sys.stdin.readline

a = [0 for _ in range(33)]
for i in range(21):
    a[i] = i+1
a[21] = 21

a[22], a[23], a[24] = 23, 24, 30
a[25], a[26] = 26, 30
a[27], a[28], a[29] = 28, 29, 30
a[30], a[31], a[32] = 31, 32, 20

move_in = [0 for _ in range(16)]
move_in[5], move_in[10], move_in[15] = 22, 25, 27

plus = [0 for _ in range(33)]
for i in range(1, 21):
    plus[i] = i * 2
plus[22], plus[23], plus[24] = 13, 16, 19
plus[25], plus[26] = 22, 24
plus[27], plus[28], plus[29] = 28, 27, 26
plus[30], plus[31], plus[32] = 25, 30, 35

def dfs(dice_index, ans):
    global max_ans
    if dice_index == 10:
        max_ans = max(max_ans, ans)
        return

    for i in range(4):
        x, x0, move = chess[i], chess[i], dice[dice_index]

        if x == 5 or x == 10 or x == 15:
            x = move_in[x]
            move -= 1

        if x + move <= 21:
            x += move
        else:
            for _ in range(move):
                x = a[x]

        if c[x] and x != 21:
            continue

        c[x0], c[x], chess[i] = 0, 1, x
        dfs(dice_index + 1, ans + plus[x])
        c[x0], c[x], chess[i] = 1, 0, x0

dice = list(map(int, input().split()))
chess = [0 for _ in range(4)]
c = [0 for _ in range(33)]

max_ans = 0
dfs(0, 0)
print(max_ans)
'''