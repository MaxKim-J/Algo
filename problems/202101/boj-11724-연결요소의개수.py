from collections import deque

N, M = map(int, input().split())
visited = [True] + [False] * (N)
graph = {i+1: [] for i in range(N)}

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def BFS(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


count = 0
root = 1
keep = True
true_count = 0

# 이거 좀...모든 배열의 값을 평가하는 그런 함수 없나 filter밖에 없음?
for _ in range(N):
    if true_count == N:
        break
    BFS(root)
    count += 1
    true_count = 0
    for i in range(1, N+1):
        if visited[i] == False:
            root = i
            break
        else:
            true_count += 1

print(count)


'''
시간초과 유니언 파인드...답은 나옴

def find(x):
    while parent[x] != x:
        x = find(parent[x])
    return x


def union(x, y):
    x_parent = find(x)
    y_parent = find(y)
    if x_parent != y_parent:
        parent[y_parent] = x_parent


N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    union(n1, n2)

count = 0
for i in range(1, N+1):
    if parent[i] == i:
        count += 1

print(count)
'''
