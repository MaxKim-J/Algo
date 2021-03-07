# 이어져있는 정점이라면 같이 해킹할 수 있다 => 가장 많은 연결요소를 찾으면 됨
# Pypy3

from collections import deque

n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
  x, y = map(int, input().split())
  adj[y].append(x)

def bfs(v):
  q = deque([v])
  visited = [False] * (n+1)
  visited[v] = True
  count = 1
  while q:
    v = q.popleft()
    for e in adj[v]:
      if not visited[e]:
        q.append(e)
        visited[e] = True
        count += 1

  return count

result = []
max_value = -1

for i in range(1, n+1):
  c = bfs(i)
  if c > max_value:
    result = [i]
    max_value = c
  # BFS를 여러번 시도하는데 같은 연결요소에 있는 것들은 모두 다 답으로 간주할 수 있다
  elif c == max_value:
    result.append(i)
    max_value = c

for e in result:
  print(e, end="")