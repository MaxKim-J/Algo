n, k = map(int, input().split(' '))
# BFS로 푸는게 젤 나을듯? => 하나의 그래프라고 생각하자 => 그러면 큐가 필요하고..
# 그러면 같은 깊이(초)를 가진 얘들을 한번에 순회하는 방법으로 효율적으로 문제를 풀 수 있음
# 꼭 선형적으로 초를 늘리며 생각을 할 필요는 없는 것 같다
# 트리는 반복되는 순회의 가짓수를 줄여주는 좋은 역할을 하는듯

queue = []
visited = [0 for _ in range(100001)]
depth = []
depth.append(0)
queue.append(n)

while True:
    x = queue.pop(0)
    xc = depth.pop(0)
    # 방문을 했었던 숫자는 이미 거기서 취할 수 있는 동작의 경우의 수를 다 따져봤기 때무네 패스
    # 노드의 값이 곧 위치
    if visited[x] != 1:
        visited[x] = 1
        if x-1 >= 0:
            queue.append(x-1)
            depth.append(xc + 1)
        if 2*x <= 100000:
            queue.append(2*x)
            depth.append(xc + 1)
        if x+1 <= 100000:
            queue.append(x+1)
            depth.append(xc + 1)
    if x == k:
        print(xc)
        break
