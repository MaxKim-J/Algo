# 각 좌표에서의 이동 양상은 한번씩만 평가되면 된다 => 그 다음을 또 큐에 넣게 되면 낭비가 생김
# 방문을 했었던 숫자는 이미 거기서 취할 수 있는 동작의 경우의 수를 다 따져봤기 때무네 패스

from collections import deque 

n, k = map(int, input().split(' '))
queue = deque([(n,0)])
visited = [0 for _ in range(100001)]

while True:
	x, depth = queue.popleft()
	# 방문을 하지 않은 좌표인 경우 => BFS
	if visited[x] != 1:
		visited[x] = 1
		if x-1 >= 0:
			queue.append((x-1, depth + 1))
		if 2*x <= 100000:
			queue.append((2*x, depth + 1))
		if x+1 <= 100000:
			queue.append((x+1, depth + 1))
	if x == k:
		print(depth)
		break
