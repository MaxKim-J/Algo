ar, ac, k = map(int, input().split())

board = []

for _ in range(3):
  board.append(list(map(int, input().split())))

R = C = 3
time = 0

def arr_sort(dic):
  result = []
  sorted_arr = sorted(dic.items(), key = lambda x:(x[1], x[0]))
  for num,freq in sorted_arr:
    result.append(num)
    result.append(freq)
  return result

def check_freq(freq, board):
  if board[r][c] != 0:
    if freq.get(board[r][c]):
      freq[board[r][c]] += 1
    else:
      freq[board[r][c]] = 1

while True:
  if time > 100:
    time = -1
    break
  
  if -1 < ar-1 < R and -1 < ac-1 < C and board[ar-1][ac-1] == k:
    break

  time += 1
  max_line = 0

  if R >= C:
    for r in range(R):
      freqR = dict()
      for c in range(C):
        check_freq(freqR, board)

      new_line = arr_sort(freqR)
      new_line_len = len(new_line)
      max_line = max(new_line_len, max_line)
      board[r] = new_line
    
    for r in range(R):
      for _ in range(max_line - len(board[r])):
        board[r].append(0)
    C = max_line

  else:
    for c in range(C):
      freqC = dict()
      for r in range(R):
        check_freq(freqC, board)

      new_line = arr_sort(freqC)
      new_line_len = len(new_line)
      max_line = max(new_line_len, max_line)

      for _ in range(max_line - len(board)):
        board.append([0] * C)
      for r in range(len(board)):
        board[r][c] = new_line[r] if r < new_line_len else 0
    R = max_line

print(time)

