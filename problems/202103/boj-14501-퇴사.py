from collections import deque

N = int(input())
T = [0]
P = [0]

for _ in range(N):
  t, p = map(int, input().split())
  T.append(t)
  P.append(p)

def BFS(start):
  global result
  queue = deque([(start, P[start])])

  while queue:
    index, value = queue.popleft()
    result = max(result, value)
    new_index = T[index] + index
    for j in range(new_index, N+1):
      if j + T[j] <= N + 1:
        queue.append((j, value + P[j]))

result = 0

for i in range(1, N+1):
  if i + T[i] <= N + 1:
    BFS(i)

print(result)