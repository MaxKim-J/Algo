n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))

# 이런 노가다는 실수하지 않고 한번에 끝낸다는 각오로 집중해서 할것 검산은 없다
tetromino = [
  [(0, 1), (1, 0), (1, 1)], 
  [(0, 1), (0, 2), (0, 3)], 
  [(1, 0), (2, 0), (3, 0)], 
  [(1, 0), (2, 0), (2, 1)], 
  [(1, 0), (2, 0), (2, -1)],
  [(0, 1), (0, 2), (1, 0)], 
  [(0, 1), (0, 2), (1, 2)], 
  [(0, 1), (1, 1), (2, 1)], 
  [(0, 1), (1, 0), (2, 0)], 
  [(0, 1), (0, 2), (-1, 2)], 
  [(1, 0), (1, 1), (1, 2)], 
  [(1, 0), (1, 1), (2, 1)], 
  [(1, 0), (1, -1), (2, -1)], 
  [(0, 1), (-1, 1), (-1, 2)], 
  [(0, 1), (1, 1), (1, 2)], 
  [(0, 1), (0, 2), (1, 1)], 
  [(1, 0), (1, 1), (2, 0)],
  [(1, 0), (1, -1), (2, 0)], 
  [(0, 1), (0, 2), (-1, 1)]
]


result = 0

for i in range(n):
    for j in range(m):
        for block in tetromino:
            n1x, n1y = block[0]
            n2x, n2y = block[1]
            n3x, n3y = block[2]
            sum_value = -100

            if (-1 < i + n1x < n and -1 < i + n2x < n and -1 < i + n3x < n) and (-1 < j + n1y < m and -1 < j + n2y < m and -1 < j + n3y < m):
              sum_value = board[i][j] + board[i + n1x][j + n1y] + board[i + n2x][j + n2y] + board[i + n3x][j + n3y]

            result = max(result, sum_value)

print(result)