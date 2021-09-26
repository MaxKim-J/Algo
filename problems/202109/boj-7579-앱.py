'''
아이디어 접근 모두 맞아서 깔끔하게 풀리는 문제였는데
시간이 너무 오래걸린거같다(70분) 머리를 빨리빨리 움직이자...
inf는 시간에 그렇게 큰 영향은 안미치는데 메모리에 좀 더 영향을 미치는 경향이 있다
'''

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_memory = sum(memory)
total_cost = sum(cost)
goal = total_memory - M

dp = [[10000000]*(total_cost+1) for _ in range(len(memory))]

dp[0][cost[0]] = total_memory - memory[0]
dp[0][0] = total_memory

for i in range(1, len(memory)):
  for j in range(total_cost+1):
    dp[i][j] = min(dp[i][j], dp[i-1][j])
    if dp[i-1][j] != 10000000:
      dp[i][j+cost[i]] = min(dp[i][j+cost[i]], dp[i-1][j] - memory[i])

for i in range(total_cost+1):
  if dp[-1][i] <= goal:
    print(i)
    break