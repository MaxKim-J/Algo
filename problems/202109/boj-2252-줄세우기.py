from collections import deque

n, m = map(int, input().split())

arr = []
inDegree = [ 0 for i in range(32001)]
graph = [[] for i in range(32001)] 
queue = deque()

for i in range(m):
  a, b = map(int, input().split())
  arr.append([a, b])
  
for a, b in arr: 
  inDegree[b] += 1
  graph[a].append(b)
  
for i in range(1, n + 1):
  if inDegree[i] == 0:
    queue.append(i)
    
while queue:
  student = queue.popleft() 
  # 방문하면서 진입간선 차수를 떨어트린다
  for j in graph[student]: 
    inDegree[j] -= 1
    # 새로 0이 된 얘들은 큐에 넣는다
    if inDegree[j] == 0:
      queue.append(j)

  print(student, end = ' ')

