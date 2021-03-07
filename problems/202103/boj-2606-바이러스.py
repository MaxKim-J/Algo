# 연결되어있는 모든 노드중에 가장 많은 그룹의 노드 개수를 출력
# BFS-재귀함수를 적게 쓰는데서 오는 이점이 있음

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
  x, y = map(int, input().split())
  adj[x].append(y)
  adj[y].append(x)

def dfs(now_pos):
  global count
  count += 1
  visited[now_pos] = True
  for next_pos in adj[now_pos]:
    if not visited[next_pos]:
      dfs(next_pos)

dfs(1)
print(count - 1) # 시작하는 정점을 빼기
