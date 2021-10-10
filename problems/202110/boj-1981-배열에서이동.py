from collections import deque
import sys

'''
못품ㅜ
범위 값을 이동시키면서 거기에 해당되는 경로만 탐색하면 시간 안에 돌아가는 문제였따
시간이랑 DP만 생각하느라 BFS 백트랙킹을 하는 좋은 방법을 생각하지 못한 것 같다 이렇게 풀 수도 있구나..
좀더 정답 지향적으로 생각하는게 역시 좋겠다
'''

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(): # 그냥 평범한 BFS
    q = deque()
    c = [[0]*n for _ in range(n)]
    q.append([0, 0])
    c[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 좌우값의 범위를 미리 결정해두고 지나가는 경로가 이를 만족하는 친구일때만
                # 경로를 개척한다
                # 그리고 그 경로를 통해 목적지까지 갈 수 있는지도 체크
                if left <= a[nx][ny] <= right and not c[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])
    return 0

n = int(input())

a, r_max, l_min = [], 0, sys.maxsize

for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    l_min = min(l_min, min(row)) # 보드 통틀어서 최소값
    r_max = max(r_max, max(row)) # 보드 통틀어서 최대값

# 최초의 max, min값, 꼭 포함해야 하는 값이기도 함
l_max = min(a[0][0], a[n-1][n-1])
r_min = max(a[0][0], a[n-1][n-1])

left, right = l_min, r_min
ans = sys.maxsize

while l_min <= left <= l_max and r_min <= right <= r_max:
    if bfs(): # 순회할 수 있다면
        ans = min(ans, right - left)
        left += 1 # 순회할 수 있다면 왼쪽 값을 하나 올린다음에 또 해본다
    else: # 순회할 수 없음
        right += 1 # 순회할 수 없으면 오른쪽 값을 하나 올린다(이런 식으로 범위 맞춰감)

print(ans)