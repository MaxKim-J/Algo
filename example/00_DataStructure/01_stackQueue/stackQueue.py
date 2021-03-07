# stack
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조 LIFO
stack = []

def push(data):
  stack.append(data)

# 걍 리스트에 팝써도 됨
def pop():
  data = stack[-1]
  del stack[-1]
  return data

# queue
# 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조 FIFO
queue = []

def enqueue(data):
  queue.append(data)

def dequeue():
  data = queue[0]
  del queue[0]
  return data
